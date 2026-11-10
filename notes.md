## Варианты запуска и отладки тестов:

- сам запуск происходит по команде `pytest`
- для возможности просмотра в окне браузера: `pytest --headed`.
- смена браузера: `pytest --browser название браузера`
- отдельный тест: `pytest test_login.py`
- конкретные тесты: `pytest tests/test_todo_page.py tests/test_landing_page.py`
- параллельный запуск: `pytest --numprocesses 2` (кол-во ядер цп, лучше использовать половину)
- отладочные тесты: `PWDEBUG=1 pytest -s test_example.py`

---

## Программа просмотра трассировки:

`Playwright Trace Viewer` - это графический инструмент, позволяющий просматривать записанные трассировки тестов Playwright, то есть вы можете перемещаться вперед и назад по каждому действию теста и визуально видеть, что происходило во время каждого действия.

Трассировку можно записать, запустив тесты с соответствующим `--tracing` флагом.

```bash
pytest --tracing on
```

Варианты отслеживания:
`on`, `off` (не записывать, по умолч), `retain-on-failure`.

Открытие трасировки:

```bash
playwright show-trace trace.zip
```

---

## Справочник по плагину Pytest

### Аргументы командной строки

- `--headed`: Запуск тестов в режиме с графическим интерфейсом (по умолчанию: без графического интерфейса).
- `--browser`: Запуск тестов в другом браузере chromium, firefox, или webkit. Его можно указать несколько раз (по умолчанию: chromium).
- `--browser-channel` Канал браузера , который будет использоваться.
- `--slowmo` Замедляет работу программы Playwright на указанное количество миллисекунд. Полезно для того, чтобы вы могли видеть, что происходит (по умолчанию: 0).
- `--device` Устройство, которое необходимо эмулировать.
- `--output` Каталог для артефактов, созданных тестами (по умолчанию: test-results).
- `--tracing` Следует ли записывать трассировку для каждого теста. `on`, `off`, или `retain-on-failure` (по умолчанию: `off`).
- `--video` Следует ли записывать видео для каждого теста. `on`, `off`, или `retain-on-failure` (по умолчанию: `off`).
- `--screenshot` Автоматически ли делать снимок экрана после каждого теста. `on`, `off`, или `only-on-failure` (по умолчанию: `off`).
- `--full-page-screenshot` Следует ли делать снимок экрана всей страницы в случае сбоя. По умолчанию делается снимок только области просмотра. Требуется `--screenshot` включить эту функцию (по умолчанию: `off`).

### Фиксаторы

Этот плагин настраивает специфические для Playwright тестовые фикстуры для `pytest` . Чтобы использовать эти фикстуры, укажите их имя в качестве аргумента функции `test`.

```python
def test_my_app_is_working(fixture_name):
    pass
    # Test using fixture_name
    # ...
```

### Параллелизм: выполнение нескольких тестов одновременно.

```bash
# install dependency
pip install pytest-xdist
# use the --numprocesses flag
pytest --numprocesses auto
```

### Использование различных контекстов

Для имитации работы нескольких пользователей можно создать несколько `BrowserContext` экземпляров.

```python
from playwright.sync_api import Page, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback

def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    page.goto("https://example.com")
    context = new_context()
    page2 = context.new_page()
    # page and page2 are in different contexts
```

### Настроить базовый URL

```bash
pytest --base-url http://localhost:8080
```

```python
def test_visit_example(page):
    page.goto("/admin")
    # -> Will result in http://localhost:8080/admin
```

### Использовать пользовательский размер области просмотра

```python
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
```
