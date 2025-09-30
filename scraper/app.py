import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def main():
    url = os.getenv("URL")
    if not url:
        print(json.dumps({"error": "URL not set"}))
        return

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.binary_location = "/usr/bin/chromium"  # системний Chromium

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Чекаємо, поки body містить текст
    try:
        WebDriverWait(driver, 15).until(
            lambda d: len(d.find_element("tag name", "body").text.strip()) > 0
        )
    except Exception:
        pass  # таймаут пройшов, беремо те, що є

    # JS: збираємо текст по класах елементів
    script = """
    const elements = document.querySelectorAll('[class]');
    const result = {};
    elements.forEach(el => {
        const classes = el.className.trim();
        const text = el.innerText.replace(/\\s+/g, ' ').trim();
        if (text) {
            if (result[classes]) {
                if (Array.isArray(result[classes])) result[classes].push(text);
                else result[classes] = [result[classes], text];
            } else {
                result[classes] = text;
            }
        }
    });
    return result;
    """
    result = driver.execute_script(script)

    # Опціональний скріншот
    if os.getenv("TAKE_SCREENSHOT", "0") == "1":
        driver.save_screenshot("/output/page_screenshot.png")

    # Зберігаємо JSON
    json_path = "/output/page_text.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # Вивід у stdout (чистий JSON)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    driver.quit()

if __name__ == "__main__":
    main()
