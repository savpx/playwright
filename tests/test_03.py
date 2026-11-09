# Савельев Тимур Евгеньевич
# 09.11.2026 / Время: 22:31
# Код созданный с помощью команды playwright codegen https://github.com/
# C помощью этой команды можно записывать действия пользователя на сайте и генерировать код для тестов.
# Код из раздела Generating tests, запуск локальный.
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) # запуск браузера
    context = browser.new_context() 
    page = context.new_page()
    page.goto("https://github.com/") # сайт на котором будет выполняться тест
    page.get_by_role("button", name="Developers").click() # нажатие на кнопку Developers
    page.get_by_role("link", name="Trending repos").click() # нажатие на ссылку Trending repos
    page.get_by_role("link", name="anthropics / skills").click() # нажатие на ссылку с названием репозитория антропик скилс
    page.get_by_role("link", name="Pull requests  (1.1k)").click() # нажатие на Pull requests

    context.close() # закрытие контекста браузера
    browser.close() # закрытие браузера


with sync_playwright() as playwright:
    run(playwright) 
# результат запуска: img/test_03
# код выполнен без ошибок.