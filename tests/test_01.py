# Савельев Тимур Евгеньевич
# 09.11.2026 / Время: 15:17
# Описание: код запускает браузер Chromium, открывает страницу https://playwright.dev/ и проверяет наличие заголовка Playwright и ссылки Get started, а также проверяет видимость заголовка "Installation" после перехода по ссылке.
# Код из раздела Writing Tests, запуск локальный.
import playwright
from playwright.sync_api import Page, expect
import re


# def test_has_title(page: Page):
  #  page.goto("https://playwright.dev/")

    
  #  expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
   # page.goto("https://playwright.dev/")

    
   # page.get_by_role("link", name="Get started").click()

    
    #expect(page.get_by_role("heading", name="Installation")).to_be_visible() # 
# Результат запуска: img/test_01
# Код выполнен без ошибок.


# свой тест, хочу проверить сайт википедии и нажатие на кнопку Русский
def test_get_started_link(page: Page): # Функция для теста
    page.goto("https://www.wikipedia.org/") # Переход на главную страницу Википедии
    page.get_by_role("link", name="Русский").click() # Нажатие на кнопку
    expect(page).to_have_title(re.compile("Википедия")) # Проверка что открылась страница с заголовком Википедия
# результат запуска: img/test_01_1
# код выполнен без ошибок.