Page Capture Docker

Цей проект дозволяє отримати видимий текст сайту у форматі JSON (ключ = клас елемента) та скріншот сторінки за допомогою headless Chromium у Docker-контейнері.

Весь процес відбувається локально, без додаткових завантажень Chromium під час запуску контейнера.

Особливості

JSON формує ключі по класах елементів (class).

Дублікати класів зберігаються як список.

Скриншот сторінки можна робити опційно через змінну оточення TAKE_SCREENSHOT.

В stdout тільки JSON, ніяких служебних повідомлень.

Chromium та ChromeDriver предустановлені → швидко і економно щодо трафіку.

Docker Image

Python 3.11

Selenium 4.13.0

Chromium + ChromeDriver (через apt)

Використання
1. Клонувати репозиторій
git clone <repository-url>
cd <repository-folder>

2. Побудувати Docker образ
docker build -t page-capture-final .

3. Запуск контейнера
docker run --rm -e URL="https://example.com" -v "$(pwd)/out:/output" page-capture-final


JSON виводиться у stdout та зберігається у /output/page_text.json.

4. Опціональний скриншот
docker run --rm -e URL="https://example.com" -e TAKE_SCREENSHOT=1 -v "$(pwd)/out:/output" page-capture-final


Скриншот сторінки зберігається у /output/page_screenshot.png.

Параметри
Змінна оточення	Опис
URL	Адреса сайту для сканування (обов’язково).
TAKE_SCREENSHOT	Якщо 1, робиться скриншот сторінки (опціонально).
Файли проекту

Dockerfile — опис Docker-контейнера.

app.py — основний скрипт, який збирає текст та скриншот.

/output — директорія для JSON та скріншоту (мапа на хост).
