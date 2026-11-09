# Савельев Тимур Евгеньевич
# 09.11.2026 / Время: 15:17
# Описание: код запускает браузер Chromium, открывает страницу https://playwright.dev/ и проверяет наличие заголовка Playwright и ссылки Get started, а также проверяет видимость заголовка "Installation" после перехода по ссылке.
# Код из раздела Writing Tests, запуск локальный.
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    
    page.get_by_role("link", name="Get started").click()

    
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
# Результат запуска: 2 passed, 1 warning in 9.71s
# Код выполнен без ошибок.
