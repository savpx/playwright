# Савельев Тимур Евгеньевич
# 15.11 / 14:43
# Код из раздела Эмуляция | Полноценного кода не было, поэтому собрал легкий код с открытием википедии на разрешении экрана Айфона 13 и нажатием на кнопку англ.
# Запуск локальный 

from playwright.sync_api import sync_playwright

def test_open_wikipedia_on_iphone_13():
    with sync_playwright() as p:
        iphone = p.devices["iPhone 13"] # выбор устройства iPhone 13
        browser = p.chromium.launch(headless=False) # запуск браузера
        context = browser.new_context(**iphone) # создание контекста с настройками iPhone 13
        page = context.new_page() # создание страницы
        page.goto("https://www.wikipedia.org/") # переход на страницу Википедии
        page.get_by_role("link", name="English").click() # нажатие на англ кнопку
        assert "en.wikipedia.org" in page.url # проверка что в ссылке есть en.wikipedia.org
        browser.close() # закрытие браузера

# Код выполнен без ошибок | Результат - img/test_06.png
    