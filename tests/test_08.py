# Савельев Тимур Евгеньевич
# 15.11 / 19:04
# Код из раздела Загрузки | Полноценного кода в разделе нету, поэтому я просто проверю скачивание зип файла моего репозитория c помощью функции скачивания expect_download.
# Запуск локальный 

from playwright.sync_api import Page, expect

def test_download(page: Page):
    page.goto("https://github.com/savpx/freecodecamp_vibecode") # переход на страницу репозитория
    with page.expect_download() as download_info: 
        page.get_by_role("button", name="Code").click()
        page.get_by_text("Download ZIP").click()
    download = download_info.value # получение информации о загрузке
    download.save_as("downloads/" + download.suggested_filename) # сохранение загруженного файла
    
# Код выполнен без ошибок | Результат - img/test_08.png