# Савельев Тимур Евгеньевич
# 12.11 / 15:16
# Код из раздела Getting started - Library | main.py создан для того чтобы проверить функцию создания автономных файлов, тобишь перевод в .exe файл через pyinstaller.
# Запуск локальный
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="example.png")
    browser.close()

# тот же самый код из test_04.py.
# создался файл main.exe при запуске которого активируется тест из main.py
# код выполнен без ошибок. main.exe находится в папке tests.
