## --- Мой конспект по Playwright Python | Савельев ---

# Раздел: Действия

### Текстовое поле
`page.get_by_role("textbox").fill("Peter")` - ввод текста.
`page.get_by_label("Birth date").fill("2020-02-02")` - ввод даты.
`page.get_by_label("Appointment time").fill("13:15")` - ввод времени.
`page.get_by_label("Local time").fill("2020-03-02T05:15")` - ввод лок времени.

### Флажки и переключатели
`page.get_by_label('I agree to the terms above').check()` - Установить флажок.
`expect(page.get_by_label('Subscribe to newsletter')).to_be_checked()` - Подтвердить отмеченное состояние.
`page.get_by_label('XL').check()` - Выбрать переключатель.

### Выбор параметров
`page.get_by_label('Choose a color').select_option('blue')` - Выбор одного значения, соответствующего значению или метке.
`page.get_by_label('Choose a color').select_option(label='Blue')` - Выбор одного элемента, соответствующего метке.
`page.get_by_label('Choose multiple colors').select_option(['red', 'green', 'blue'])` - Выбор нескольких.

### Щелчок мыши
`page.get_by_role("button").click()` - общий щелчок
`page.get_by_text("Item").dblclick()` - двойной клик
`page.get_by_text("Item").click(button="right")` - правый клик
`page.get_by_text("Item").click(modifiers=["Shift"])` - клик со шифтом
`page.get_by_text("Item").hover()` - Наводка курсора на элемент
`page.get_by_text("Item").click(position={ "x": 0, "y": 0})` - клик по позиции
`page.get_by_role("button").click(force=True)` - принудительный клик
`page.get_by_role("button").dispatch_event('click')` - отправка события click без реального нажатия мышью

### Ввод посимвольно
`page.locator('#area').press_sequentially('Hello World!')` - ввод текста символ за символом

### Клавиши и сочетания
`page.get_by_text("Submit").press("Enter")` - нажатие Enter.
`page.get_by_role("textbox").press("Control+ArrowRight")` - сочетание клавиш.
`page.get_by_role("textbox").press("$")` - ввод одного символа.
`page.locator('#name').press('Shift+A')` - заглавная A.
`page.locator('#name').press('Shift+ArrowLeft')` - выделение влево.
Регистр важен, `'a'` и `'A'`

### Загрузка файлов
`page.get_by_label("Upload file").set_input_files('myfile.pdf')` - один файл.
`page.get_by_label("Upload files").set_input_files(['file1.txt', 'file2.txt'])` - несколько файлов.
`page.get_by_label("Upload directory").set_input_files('mydir')` - выбор папки.
`page.get_by_label("Upload file").set_input_files([])` - очистить выбор.
`page.get_by_label("Upload file").set_input_files(files=[{"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}])` - файл из памяти, без файла на диске.

### Фокус на элементе
`page.get_by_label('password').focus()` - перевод фокуса, для страниц, которые реагируют на focus.

### Перетаскивание
`page.locator("#item-to-be-dragged").drag_to(page.locator("#item-to-drop-at"))` - перетаскивание элемента на элемент: наведение на элемент, зажатие левой кнопки, движение до цели, отпускание.

### Прокрутка
Вручную почти не нужна, Playwright прокручивает страницу сам перед действием.
`page.get_by_role("button").click()` - кнопку доскроллит автоматически.
`page.get_by_text("Footer text").scroll_into_view_if_needed()` - прокрутка до элемента.

# Раздел: Автоматическое ожидание

### Утверждения
`expect(locator).to_be_attached()` - Элемент прикреплен.
`expect(locator).to_be_checked()` - Флажок установлен.
`expect(locator).to_be_disabled()` - Элемент отключен.
`expect(locator).to_be_editable()` - Элемент редактируемый.
`expect(locator).to_be_empty()` - Контейнер пуст.
`expect(locator).to_be_enabled()` - Элемент включен.
`expect(locator).to_be_focused()` - Элемент в фокусе.
`expect(locator).to_be_hidden()` - Элемент не виден.
`expect(locator).to_be_in_viewport()` - Элемент пересекает область просмотра.
`expect(locator).to_be_visible()` - Элемент виден.
`expect(locator).to_contain_text()` - Элемент содержит текст.
`expect(locator).to_have_attribute()` - Элемент имеет атрибут DOM.
`expect(locator).to_have_class()` - Элемент имеет свойство класса.
`expect(locator).to_have_count()` - В списке указано точное количество детей.
`expect(locator).to_have_css()` - Элемент имеет свойство CSS.
`expect(locator).to_have_id()` - Элемент имеет идентификатор.
`expect(locator).to_have_js_property()` - Элемент имеет свойство JavaScript.
`expect(locator).to_have_text()` - Элемент соответствует тексту.
`expect(locator).to_have_value()` - Входные данные имеют значение.
`expect(locator).to_have_values()` - В меню «Выбрать» выбраны параметры.
`expect(page).to_have_title()` - Страница имеет заголовок.
`expect(page).to_have_url()` - Страница имеет URL-адрес.
`expect(response).to_be_ok()` - Ответ имеет статус "ОК".

Элемент считается видимым, если он имеет непустой ограничивающий прямоугольник и не имеет visibility:hidden вычисленного стиля.
Элемент считается стабильным, если он сохраняет один и тот же ограничивающий прямоугольник как минимум в течение двух последовательных кадров анимации.
Элемент считается редактируемым, если он активирован и не является доступным только для чтения.
Элемент считается неинертным, если он не является частью инертного поддерева. Инертные элементы нельзя сфокусировать, щелкнуть по ним или иным образом с ними взаимодействовать.

# Раздел: Тестирование API
APIRequestContext может отправлять все виды HTTP(S)-запросов по сети.
пока пропущу.

# Раздел: Утверждения
Playwright включает в себя специфические для веб-среды утверждения, которые автоматически повторяют попытку до тех пор, пока не будет выполнено ожидаемое условие.
expect(page.get_by_test_id("status")).to_have_text("Submitted") - Программа Playwright будет повторно проверять элемент с тестовым ID status до тех пор, пока не получит нужный "Submitted"текст. По умолчанию время ожидания для проверок составляет 5 секунд.

### Мягкие утверждения
По умолчанию, неудачная проверка утверждения приводит к завершению выполнения теста. Playwright также поддерживает мягкие проверки утверждения : неудачные мягкие проверки утверждения не завершают выполнение теста, а помечают тест как неудачный.
expect.soft(page.get_by_test_id("status")).to_have_text("Success") - soft не остановит тест в случае неудачи.

### Установка пользовательского тайм-аута
Глобальный таймаут: 
`from playwright.sync_api import expect`
`expect.set_options(timeout=10_000)`

### Тайм-аут для каждого утверждения
`from playwright.sync_api import expect`
`def test_foobar(page: Page) -> None:`
    `expect(page.get_by_text("Name")).to_be_visible(timeout=10_000)`

# Раздел: Аунтификация
Playwright выполняет тесты в изолированных средах, называемых контекстами браузера . Такая модель изоляции повышает воспроизводимость и предотвращает каскадные сбои тестов. Тесты могут загружать существующее аутентифицированное состояние. Это устраняет необходимость аутентификации в каждом тесте и ускоряет выполнение тестов.


Мы рекомендуем создать playwright/.authкаталог и добавить его в ваш файл .gitignore. Ваша процедура аутентификации будет генерировать состояние аутентифицированного браузера и сохранять его в файл в этом playwright/.authкаталоге.
`mkdir -p playwright/.auth`

`echo $'\nplaywright/.auth' >> .gitignore`
### Вход в систему перед каждым тестом
В следующем примере выполняется вход в GitHub. После выполнения этих шагов будет выполнена аутентификация в контексте браузера.

page = context.new_page()
page.goto('https://github.com/login')

page.get_by_label("Username or email address").fill("username")
page.get_by_label("Password").fill("password")
page.get_by_role("button", name="Sign in").click()

Повторная авторизация для каждого теста может замедлить его выполнение. Чтобы этого избежать, используйте вместо этого существующее состояние аутентификации.

### Повторное использование подписанного в штате

storage = context.storage_state(path="state.json")

context = browser.new_context(storage_state="state.json")

### Расширенные сценарии
Повторное использование аутентифицированного состояния включает в себя файлы cookie , локальное хранилище , IndexedDB и аутентификацию на основе пароля ( WebAuthn ). 

import os

session_storage = page.evaluate("() => JSON.stringify(sessionStorage)")
os.environ["SESSION_STORAGE"] = session_storage

session_storage = os.environ["SESSION_STORAGE"]
escaped_session_storage = session_storage.replace("\\", "\\\\").replace("'", "\\'")
context.add_init_script("""(storage => {
  if (window.location.hostname === 'example.com') {
    const entries = JSON.parse(storage)
    for (const [key, value] of Object.entries(entries)) {
      window.sessionStorage.setItem(key, value)
    }
  }
})('""" + escaped_session_storage + "')")


Раздел Браузеры
Для работы каждой версии Playwright требуются определённые версии исполняемых файлов браузера. Для установки этих браузеров вам понадобится использовать интерфейс командной строки Playwright.

playwright install
playwright install webkit - установка опред браузера

### Установите системные зависимости
Системные зависимости могут устанавливаться автоматически. Это полезно для сред непрерывной интеграции (CI).
playwright install-deps
playwright install-deps chromium - для конкретного браузера

Playwright может запускать тесты в браузерах Chromium, WebKit и Firefox, а также в фирменных браузерах, таких как Google Chrome и Microsoft Edge.
pytest test_login.py --browser webkit - запуск в конкретном браузере.
pytest test_login.py --browser webkit --browser firefox - в нескольких.

Иногда компании используют внутренний прокси-сервер, который блокирует прямой доступ к общедоступным ресурсам. В этом случае Playwright можно настроить на загрузку браузеров через прокси-сервер.
pip install playwright
HTTPS_PROXY=https://192.0.2.1 playwright install (Bash)

Иногда компании используют внутренний репозиторий артефактов для размещения исполняемых файлов браузера. В этом случае Playwright можно настроить на загрузку из пользовательского места с помощью PLAYWRIGHT_DOWNLOAD_HOSTпеременной окружения.
pip install playwright
PLAYWRIGHT_DOWNLOAD_HOST=http://192.0.2.1 playwright install 

Удаление устаревших браузеров
Чтобы отказаться от удаления неиспользуемых браузеров, вы можете установить PLAYWRIGHT_SKIP_BROWSER_GC=1переменную среды или передать этот --no-removeпараметр команде установки:
playwright install --no-remove

Выводит список браузеров со всех установленных на компьютере приложений Playwright:
playwright install --list

Это удалит браузеры (Chromium, Firefox, WebKit) из текущей установки Playwright:
playwright uninstall

Чтобы удалить браузеры и из других установок Playwright, передайте --allфлаг:
playwright uninstall --all