import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs

def main():
    url = os.getenv("URL")
    if not url:
        raise ValueError("Змінна URL не задана")

    # Налаштування браузера для запуска в Docker
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.binary_location = "/usr/bin/chromium"  # системний Chromium

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        
        #print("Посилання:", url)
        
        button_text = "Streaming widget"

        # Ищем кнопку по тексту и кликаем
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                f"//div[contains(@class,'widget-button-icon-text') "
                f"and normalize-space(text())='{button_text}']"
                f"/ancestor::div[@class='widget-button']"
            ))
        )

        #print("Кнопка:", button)

        original_windows = driver.window_handles
        # button.click()
        driver.execute_script("arguments[0].click();", button)

        # Ждём новое окно
        WebDriverWait(driver, 10).until(
            EC.new_window_is_opened(original_windows)
        )

        # Переходимо на нове окно
        new_window = [w for w in driver.window_handles if w not in original_windows][0]
        driver.switch_to.window(new_window)

        new_url = driver.current_url
        #print("Посилання з нового окна:", new_url)
        
        # Парсим longJarId
        parsed = urlparse(new_url)
        params = parse_qs(parsed.query)
        longJarId = params.get("longJarId", [None])[0]

        print(longJarId)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
