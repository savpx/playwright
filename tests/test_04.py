# Савельев Тимур Евгеньевич
# 11.11 / 22:47
# Код из раздела Getting started - Library | Выполняет запуск браузера, открытие страницы, после скриншот страницы.
# Запуск локальный

from playwright.sync_api import sync_playwright

#with sync_playwright() as p: 
    #browser = p.webkit.launch() # запуск браузера
    #page = browser.new_page() # новая вкладка
    #page.goto("https://playwright.dev/") # открытие сайиа
    #page.screenshot(path="example.png") # сделать скриншот и сохранить с названием example
    #browser.close() # закрытие и завершение теста

# Код выполнен без ошибок. Скриншот: img/test_04.png


# Переделаный код: Задача открыть Википедию в хромиум, выбрать Русский, выбрать Обсуждение, сделать скриншот под названием test_04_1
with sync_playwright() as p: 
    browser = p.chromium.launch() # запуск браузера
    page = browser.new_page() # новая вкладка
    page.goto("https://www.wikipedia.org/") # Википедия
    page.get_by_role("link", name="Русский").click() # Нажатие на Русский
    page.get_by_role("link", name="Обсуждение").click() # Нажатие на Обсуждение
    page.screenshot(path="test_04_1.png") # сделать скриншот и сохранить с названием test_04_1
    browser.close() # закрыть

# Код выполнен без ошибок. Результат: img/test_04_1.png