# Савельев Тимур Евгеньевич
# 12.11 / 14:44
# Код из раздела Getting started - Library | тот же самый код что и в test_04, но тут проверяется возможность режима REPL, когда в терминал вводишь каждую строчку по очереди, проверяя поэтапно.
# Запуск локальный. Для начала надо вводить Python в терминал.

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example.png")
browser.close()
playwright.stop()

# Код выполнен без ошибок.