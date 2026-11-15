# Савельев Тимур Евгеньевич
# 14.11 / 11:17
# Код из раздела Аутентификация | Выполняет авторизацию в гитхабе.
# Запуск локальный

from playwright.sync_api import Page, expect

# Код был переписан под функцию, чтобы запуск был через pytest
# def test_github_login(page: Page):
    #page.goto("https://github.com/login") # ссылка на вход гитхаб
    #page.get_by_label("Username or email address").fill("username") # Ввод username в поле логина
    #page.get_by_label("Password").fill("password") # Ввод password в поле пароля
    #page.get_by_role("button", name="Sign in").click() # нажатие на кнопку Войти

# Код выполнен без ошибок. Скриншот: img/test_05.png

# Улучшенный код. Вход на страницу википедии, нажатие на кнопку Английский, нажатие на кнопку Create account и сама регистрация.
def test_wikipedia(page: Page):
    page.goto("https://www.wikipedia.org/") # ссылка на регистрацию гитхаб
    page.get_by_role("link", name="English").click() # нажатие на кнопку Английский
    page.get_by_role("link", name="Create account").first.click() # нажатие на кнопку Create account, из за того что находилось две кнопки Create account, прописал first.click.
    page.get_by_placeholder("Enter your username").fill("savpx")
    page.get_by_placeholder("Enter a password").fill("password")
    page.get_by_placeholder("Enter password again").fill("password")
    page.get_by_placeholder("Enter your email address").fill("email@example.com") # Ввод email в поле регистрации
    page.get_by_role("button", name="Create your account").click() # нажатие на кнопку Создать аккаунт

# так как на википедии в полях ввода есть подсказки, пришлось переписать не на get_by_label, а на get_by_placeholder.
# Код выполнен без ошибок. Скриншот: img/test_05_1.png