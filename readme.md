# EN

## Page Capture Docker

This project allows you to obtain **visible text from a website in JSON format** (key = element class) and a **page screenshot** using **headless Chromium** in a Docker container.  

The entire process runs **locally**, without additional Chromium downloads when starting the container.  

---

### Features

- JSON keys are formed based on **element classes** (`class`).  
- Duplicate classes are stored as a list.  
- Page screenshot can be taken **optionally** via the environment variable `TAKE_SCREENSHOT`.  
- Only **JSON is printed to stdout**, no service messages.  
- Chromium and ChromeDriver are **pre-installed** → fast and bandwidth-efficient.  

---

### Docker Image

- Python 3.11  
- Selenium 4.13.0  
- Chromium + ChromeDriver (installed via `apt`)  

---

### Usage

#### 1. Clone the repository

```bash
git clone https://github.com/wyorf/page-capture.git
cd page-capture
```

#### 2. Build the Docker image
```docker build -t page-capture ./scraper```

#### 3. Run the container
```docker run --rm -e URL="https://example.com" -v "$(pwd)/out:/output" page-capture```
The JSON output is printed to stdout and saved to /output/page_text.json.

#### 4. Optional screenshot (mainly for debug)
```docker run --rm -e URL="https://example.com" -e TAKE_SCREENSHOT=1 -v "$(pwd)/out:/output" page-capture```

The page screenshot is saved to /output/page_screenshot.png.

### Environment Variables
- Variable	Description
- URL	The website URL to capture (required).
- TAKE_SCREENSHOT	Set to 1 to take a page screenshot (optional).



# UA

## Page Capture Docker

Цей проект дозволяє отримати **видимий текст сайту у форматі JSON** (ключ = клас елемента) та **скріншот сторінки** за допомогою **headless Chromium** у Docker-контейнері.  

Весь процес відбувається **локально**, без додаткових завантажень Chromium під час запуску контейнера.  

---

### Особливості

- JSON формує ключі по **класах елементів** (`class`).  
- Дублікати класів зберігаються як список.  
- Скриншот сторінки можна робити **опційно** через змінну оточення `TAKE_SCREENSHOT`.  
- В stdout **тільки JSON**, ніяких служебних повідомлень.  
- Chromium та ChromeDriver **предустановлені** → швидко і економно щодо трафіку.  

---

### Docker Image

- Python 3.11  
- Selenium 4.13.0  
- Chromium + ChromeDriver (через `apt`)  

---

### Використання

#### 1. Клонувати репозиторій

```bash
git clone <repository-url>
cd <repository-folder>
```

#### 2. Побудувати Docker образ
```docker build -t page-capture .```

#### 3. Запуск контейнера
```docker run --rm -e URL="https://example.com" -v "$(pwd)/out:/output" page-capture```


JSON виводиться у stdout та зберігається у /output/page_text.json.

#### 4. Опціональний скриншот
```docker run --rm -e URL="https://example.com" -e TAKE_SCREENSHOT=1 -v "$(pwd)/out:/output" page-capture```


Скриншот сторінки зберігається у /output/page_screenshot.png.

### Параметри
- Змінна оточення	Опис
- URL	Адреса сайту для сканування (обов’язково).
- TAKE_SCREENSHOT	Якщо 1, робиться скриншот сторінки (опціонально).

### Файли проекту

- Dockerfile — опис Docker-контейнера.
- app.py — основний скрипт, який збирає текст та скриншот.
- /output — директорія для JSON та скріншоту (мапа на хост).
