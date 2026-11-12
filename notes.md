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

### Тестирование API
APIRequestContext может отправлять все виды HTTP(S)-запросов по сети.
пока пропущу.

### Утверждения
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

### Аунтификация
