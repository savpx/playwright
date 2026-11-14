# Савельев Тимур Евгеньевич
# 14.11 / 11:17
# Код из раздела Аутентификация | Выполняет авторизацию в гитхабе.
# Запуск локальный
from playwright.sync_api import Page, expect
# Код был переписан под функцию, чтобы запуск был через pytest
def test_github_login(page: Page):
    page.goto("https://github.com/login") # ссылка
    page.get_by_label("Username or email address").fill("username") # Ввод username в поле логина
    page.get_by_label("Password").fill("password") # Ввод password в поле пароля
    page.get_by_role("button", name="Sign in").click() # нажатие на кнопку Войти

# Код выполнен без ошибок. Скриншот: img/test_05.png