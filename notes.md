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
`expect.soft(page.get_by_test_id("status")).to_have_text("Success")` - soft не остановит тест в случае неудачи.

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

`page = context.new_page()`
`page.goto('https://github.com/login')`

`page.get_by_label("Username or email address").fill("username")`
`page.get_by_label("Password").fill("password")`
`page.get_by_role("button", name="Sign in").click()`

Повторная авторизация для каждого теста может замедлить его выполнение. Чтобы этого избежать, используйте вместо этого существующее состояние аутентификации.

### Повторное использование подписанного в штате

`storage = context.storage_state(path="state.json")`

`context = browser.new_context(storage_state="state.json")`

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


# Раздел: Браузеры
Для работы каждой версии Playwright требуются определённые версии исполняемых файлов браузера. Для установки этих браузеров вам понадобится использовать интерфейс командной строки Playwright.

`playwright install`
`playwright install webkit` - установка опред браузера

### Установите системные зависимости
Системные зависимости могут устанавливаться автоматически. Это полезно для сред непрерывной интеграции (CI).
`playwright install-deps`
`playwright install-deps chromium` - для конкретного браузера

Playwright может запускать тесты в браузерах Chromium, WebKit и Firefox, а также в фирменных браузерах, таких как Google Chrome и Microsoft Edge.
`pytest test_login.py --browser webkit` - запуск в конкретном браузере.
`pytest test_login.py --browser webkit --browser firefox` - в нескольких.

Иногда компании используют внутренний прокси-сервер, который блокирует прямой доступ к общедоступным ресурсам. В этом случае Playwright можно настроить на загрузку браузеров через прокси-сервер.
`pip install playwright`
`HTTPS_PROXY=https://192.0.2.1 playwright install` (Bash)

Иногда компании используют внутренний репозиторий артефактов для размещения исполняемых файлов браузера. В этом случае Playwright можно настроить на загрузку из пользовательского места с помощью PLAYWRIGHT_DOWNLOAD_HOSTпеременной окружения.
`pip install playwright`
`PLAYWRIGHT_DOWNLOAD_HOST=http://192.0.2.1 playwright install`

### Удаление устаревших браузеров
Чтобы отказаться от удаления неиспользуемых браузеров, вы можете установить PLAYWRIGHT_SKIP_BROWSER_GC=1переменную среды или передать этот --no-removeпараметр команде установки:
`playwright install --no-remove`

Выводит список браузеров со всех установленных на компьютере приложений Playwright:
`playwright install --list`

Это удалит браузеры (Chromium, Firefox, WebKit) из текущей установки Playwright:
`playwright uninstall`

Чтобы удалить браузеры и из других установок Playwright, передайте --allфлаг:
`playwright uninstall --all`

# Расширения Chrome 
на потом


# Раздел: Часы

Позволяет управлять временем внутри тестов. Можно проверять таймеры, даты и автоматический выход из аккаунта без реального ожидания.

### Фиксированное время
`page.clock.set_fixed_time(datetime.datetime(2024, 2, 2, 10, 0, 0))` - установить фиксированное время для Date.now() и new Date(), таймеры продолжают работать.
`page.clock.set_fixed_time("2024-02-02")` - можно передать дату строкой.

### Управление временем
`page.clock.install()` - установить поддельные часы и получить возможность управлять временем.
`page.clock.pause_at(datetime.datetime(2024, 2, 2, 10, 0, 0))` - перейти к указанному времени и остановить часы.
`page.clock.fast_forward("30:00")` - перемотать время на 30 минут, срабатывают только таймеры, срок которых наступил.
`page.clock.run_for(2000)` - продвинуть время на 2 секунды, выполняя все таймеры и связанные callbacks.
`page.clock.resume()` - продолжить обычный ход времени.
`page.clock.set_system_time("2024-02-02")` - изменить системное время страницы, не вызывая таймеры.

install() нужно вызывать до других действий, связанных со временем. Часы действуют на весь контекст браузера, включая все страницы и iframe.

# Раздел: Отладочные тесты
Playwright Inspector - графический инструмент для отладки тестов. Позволяет пошагово выполнять действия, изменять локаторы и смотреть логи проверок элементов.

`PWDEBUG=1 pytest -s` - запуск тестов в режиме отладки (Bash).
`$env:PWDEBUG=1` - включить режим отладки в PowerShell.
`page.pause()` - остановить выполнение теста в указанном месте и открыть Inspector.

Inspector позволяет:
- выполнять тест по шагам или целиком
- выбирать элементы через Pick Locator
- редактировать локаторы и сразу видеть совпадения
- смотреть Actionability logs, где видно проверки видимости, доступности и стабильности элемента.

### Логи
`PWDEBUG=console pytest -s` -
`DEBUG=pw:api pytest -s` - подробные логи действий Playwright.
`chromium.launch(headless=False, slow_mo=100)` - запуск браузера с окном и замедлением каждого действия

# Раздел: Диалоги
Playwright может взаимодействовать с диалоговыми окнами веб-страницы, такими как alert, confirm, promptа также beforeunload подтверждающими запросами.

По умолчанию диалоги автоматически закрываются. Если добавить обработчик page.on("dialog"), его нужно обработать через accept() или dismiss(), иначе действие страницы зависнет.

`page.on("dialog", lambda dialog: dialog.accept())` - принять диалог.
`page.on("dialog", lambda dialog: dialog.dismiss())` - закрыть диалог без подтверждения.
`page.on("dialog", lambda dialog: print(dialog.message))` - получить текст диалога, но такой обработчик сам по себе не закрывает его.

# Раздел: Загрузки
При каждой загрузке файла страница вызывает событие download. Файл сначала сохраняется во временную папку и удаляется при закрытии BrowserContext.

### Ожидание загрузки
`with page.expect_download() as download_info:` - ожидание начала загрузки.
`page.get_by_text("Download file").click()` - действие, которое запускает загрузку.
`download = download_info.value` - получить объект загрузки.
`download.save_as("/path/to/file.pdf")` - сохранить файл в указанное место.
`download.suggested_filename` - имя файла, предложенное браузером.
`download.path()` - путь к временному файлу.

`browser_type.launch(downloads_path="downloads")` - указать папку для загрузок при запуске браузера.

# Раздел: Эмуляция
Playwright позволяет имитировать разные устройства и условия браузера: размер экрана, touch, геолокацию, язык, часовой пояс и другие параметры.

### Устройства
`browser.new_context(**playwright.devices["iPhone 13"])` - создать контекст с настройками выбранного устройства.
`browser.new_context(viewport={"width": 1280, "height": 720})` - задать размер области просмотра.
`browser.new_context(device_scale_factor=2)` - задать коэффициент плотности пикселей.
`browser.new_context(is_mobile=True, has_touch=True)` - включить мобильный режим и поддержку касаний.

### Локаль и часовой пояс
`context = browser.new_context(`
  `locale='de-DE',` - язык и регион
  `timezone_id='Europe/Berlin',` - часовой пояс
`)`

### Разрешения
`context.grant_permissions(['notifications'], origin='https://skype.com')` - Разрешить уведомления для определенного домена.
`context.clear_permissions()` - очистить разрешения.

### Геолокация
`context.set_geolocation({"longitude": 48.858455, "latitude": 2.294474})` - настройка местоположения.


### Цветовая гамма и медиа
`browser.new_context(color_scheme="dark")` - включить тёмную тему.
`browser.new_context(reduced_motion="reduce")` - имитировать настройку уменьшения анимации.
`browser.new_context(permissions=["clipboard-read"])` - выдать контексту разрешение на чтение буфера обмена.

# Раздел: Выполнение JavaScript
Python-код Playwright и JavaScript страницы работают в разных средах. Через page.evaluate() можно выполнить JavaScript в контексте страницы и получить результат обратно в Python.

`page.evaluate("() => document.location.href")` - получить текущий URL.
`page.evaluate("() => window.innerWidth")` - получить ширину окна браузера.

### Передача аргументов
`page.evaluate("(name) => document.title = name", "New title")` - передать значение из Python в JavaScript.
`page.evaluate("([a, b]) => a + b", [2, 3])` - передать список аргументов.

# Раздел: События
Playwright позволяет ожидать события страницы или подписываться на них. Например, запросы, всплывающие окна, загрузки и создание новых страниц.

### Ожидание запроса
`with page.expect_request("**/*logo*.png") as request_info:` - ожидать запрос по указанному шаблону.
`page.goto("https://wikipedia.org")` - действие, во время которого должен появиться запрос.
`request = request_info.value` - получить объект запроса.
`request.url` - адрес запроса.

### Всплывающее окно
`with page.expect_popup() as popup_info:` - ожидать открытие новой вкладки или окна.
`page.get_by_text("open the popup").click()` - действие, которое открывает окно.
`popup = popup_info.value` - получить новую страницу.

### Подписка на события
`page.on("request", lambda request: print(request.url))` - отслеживать запросы.
`page.on("response", lambda response: print(response.status))` - отслеживать ответы сервера.
`page.on("console", lambda message: print(message.text))` - получать сообщения консоли.

# Раздел: Расширяемость
Playwright поддерживает пользовательские движки селекторов. Их можно зарегистрировать через selectors.register().

Пользовательский движок должен содержать:
 query - поиск первого подходящего элемента;
 queryAll - поиск всех подходящих элементов.
`playwright.selectors.register("my-engine", engine)` - зарегистрировать собственный движок селекторов.
Регистрацию нужно выполнить до создания страницы.

# Раздел: Фреймы
Страница может содержать iframe. Для работы с ними Playwright предоставляет Frame и FrameLocator.

`page.main_frame` - главный фрейм страницы.
`page.frames` - список всех фреймов.
`page.frame_locator("#my-iframe")` - перейти к iframe по селектору.
`page.frame_locator("#my-iframe").get_by_text("Submit").click()` - найти и нажать элемент внутри iframe.

### События фреймов
`page.on("frameattached", lambda frame: print(frame.url))` - фрейм добавлен.
`page.on("framenavigated", lambda frame: print(frame.url))` - фрейм перешёл на другой адрес.
`page.on("framedetached", lambda frame: print(frame.url))` - фрейм удалён.

# Раздел: Обработчики
Handle - ссылка на объект внутри страницы. Сам объект находится в браузере, а обработчик используется из Python.

Есть два основных типа:
JSHandle - ссылка на любой объект JavaScript.
ElementHandle - ссылка на DOM-элемент, имеет дополнительные методы для работы с элементом.
`js_handle = page.evaluate_handle("window")` - получить JSHandle объекта window.
`js_handle.evaluate("window => window.location.href")` - выполнить JavaScript относительно полученного объекта.
`js_handle.json_value()` - получить сериализованное значение объекта.

Использование ElementHandle обычно не рекомендуется. Для поиска и действий лучше использовать Locator, так как он повторно ищет элемент перед действием.

# Раздел: Изоляция
Тесты Playwright выполняются в отдельных BrowserContext. Каждый контекст имеет собственные cookies, localStorage и sessionStorage.

Это позволяет запускать тесты независимо друг от друга. Ошибка одного теста не должна влиять на состояние другого.

`context = browser.new_context()` - создать отдельный контекст браузера.
`page = context.new_page()` - открыть страницу внутри контекста.
`context.close()` - закрыть контекст и его страницы.

В pytest Playwright создаёт отдельный контекст и страницу для каждого теста автоматически.

# Раздел: Локалисты
Локатор - способ найти элемент на странице. Он не ищет элемент один раз навсегда, а повторно разрешается перед каждым действием. Это помогает работать с динамическими страницами.

### Основные способы поиска
`page.get_by_role("button", name="Submit")` - поиск по роли и доступному имени.
`page.get_by_text("Welcome")` - поиск по тексту.
`page.get_by_label("Password")` - поиск по подписи поля.
`page.get_by_placeholder("Enter name")` - поиск по placeholder.
`page.get_by_test_id("submit")` - поиск по тестовому ID.
`page.locator(".item")` - поиск по CSS-селектору.

### Фильтрация
`page.locator("article").filter(has_text="Playwright")` - оставить элементы, содержащие указанный текст.
`page.locator("article").filter(has=page.get_by_role("button"))` - оставить элементы, внутри которых есть кнопка.
`page.get_by_role("listitem").filter(has_not_text="Done")` - исключить элементы с указанным текстом.

### Работа со списком
`page.get_by_role("listitem").count()` - количество найденных элементов.
`page.get_by_role("listitem").first` - первый элемент.
`page.get_by_role("listitem").last` - последний элемент.
`page.get_by_role("listitem").nth(2)` - элемент с индексом 2.
`page.get_by_role("listitem").all()` - получить список локаторов для найденных элементов. Метод не ждёт появления элементов, поэтому для динамических списков сначала нужно дождаться их загрузки.

### Вложенные локаторы
`page.locator("article").get_by_role("button", name="Read more")` - найти кнопку внутри article.
`page.locator("article").locator("h2")` - найти заголовок внутри элемента.


# Раздел: Навигация
Навигация - переход страницы на другой URL или изменение текущего документа.

`page.goto("https://example.com")` - перейти по адресу.
`page.go_back()` - вернуться на предыдущую страницу.
`page.go_forward()` - перейти вперёд.
`page.reload()` - перезагрузить страницу.
`page.url` - получить текущий URL.

### Ожидание навигации
`page.wait_for_url("**/dashboard")` - дождаться перехода на URL, подходящий под шаблон.
`page.wait_for_load_state("domcontentloaded")` - дождаться события DOMContentLoaded.
`page.wait_for_load_state("load")` - дождаться события load.
`page.wait_for_load_state("networkidle")` - ожидать отсутствие сетевых соединений минимум 500 мс. Для тестов обычно не рекомендуется, лучше проверять готовность страницы через expect.

Состояния загрузки:
commit - получен ответ и началась загрузка документа;
domcontentloaded - HTML разобран;
load - загружены ресурсы страницы;
networkidle - нет сетевой активности минимум 500 мс.

# Раздел: Сеть
Playwright позволяет отслеживать и изменять сетевой трафик браузера: HTTP-запросы, ответы, XHR и fetch.

### Запросы и ответы
`page.on("request", lambda request: print(request.url))` - отслеживать запросы.
`page.on("response", lambda response: print(response.status, response.url))` - отслеживать ответы.
`response.status` - статус ответа.
`response.ok` - успешный ли ответ.
`request.method` - HTTP-метод запроса.

### HTTP-аутентификация
`context = browser.new_context(http_credentials={"username": "bill", "password": "pa55w0rd"})` - задать данные для HTTP-аутентификации.
`page = context.new_page()` - создать страницу с этими настройками.

### Проверка ответа
`with page.expect_response("**/api/data") as response_info:` - ожидать ответ по адресу.
`page.get_by_role("button", name="Load").click()` - действие, которое вызывает запрос.
`response = response_info.value` - получить ответ.

# Раздел: Другие локаторы
Дополнительные способы поиска элементов, когда обычных локаторов недостаточно.

`page.get_by_alt_text("logo")` - поиск изображения по alt-тексту.
`page.get_by_title("Issues count")` - поиск по атрибуту title.
`page.get_by_role("heading", name="Sign up")` - поиск заголовка по роли и имени.
`page.get_by_text("Submit", exact=True)` - поиск точного текста.
`page.locator("css=button")` - CSS-селектор.
`page.locator("xpath=//button")` - XPath-селектор.

Для стабильных тестов лучше использовать локаторы по роли, подписи, тексту или test id, а не сложные CSS и XPath.

# Раздел: Страницы
Page - отдельная вкладка или окно браузера. Через объект Page выполняется большая часть действий с сайтом.

`page = context.new_page()` - создать новую страницу.
`page.goto("https://example.com")` - перейти на сайт.
`page.title()` - получить заголовок.
`page.url` - текущий адрес страницы.
`page.close()` - закрыть страницу.
`page.bring_to_front()` - сделать страницу активной.

### Вкладки и окна
`context.pages` - список открытых страниц в контексте.
`page.on("popup", lambda popup: print(popup.url))` - событие открытия всплывающей страницы.
`with page.expect_popup() as popup_info:` - ожидать новую вкладку после действия.
`popup = popup_info.value` - получить объект новой страницы.