# Playwright for Python

Репозиторий - мой конспект по изучению библиотеки **Playwright for Python**.


- `playwright` (>=1.64.1) - сама библиотека: запускает Chromium / Firefox / WebKit, ходит по страницам, кликает, делает скриншоты.
- `pytest-playwright` (>=0.10.0) - плагин, который подружил Playwright с `pytest`. Из него берутся фикстуры `page`, `context` и т.д.  поэтому в тестах не надо вручную поднимать браузер.
- `pytest` - раннер тестов.
- Python >= 3.12, зависимости зафиксированы в `pyproject.toml` и `uv.lock` (ставил через `uv`).