# Савельев Тимур Евгеньевич
# 15.11 / 19:33
# Код из раздела Видео | Полноценного кода в разделе нету, я написал код который снимает видео теста с открытием Макса.
# Запуск локальный 

from playwright.sync_api import Page, expect

def test_video(browser, page: Page):
    context = browser.new_context( # запись видео привязана к контексту браузера
    record_video_dir="videos/",
    record_video_size={"width": 640, "height": 480} 
) # задаем размер видео
    page = context.new_page() # создаем новую страницу
    page.goto("https://web.max.ru/")
    expect(page.get_by_role("button", name="Войти по номеру телефона")).to_be_visible() # проверяем видимость кнопки
    context.close() # закрываем контекст браузера
# Код выполнен без ошибок | Результат - img/test_09.png
