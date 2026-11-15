# Савельев Тимур Евгеньевич
# 15.11 / 18:54
# Код из раздела Тестирование API | Происходит подключение к API GitHub, создается репозиторий test, после чего создаются bug Issue и feature Issue, проверка результатов и удаление репозитория.
# Запуск локальный 

import os
from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"

GITHUB_USER = os.getenv("GITHUB_USER")
assert GITHUB_USER, "GITHUB_USER is not set"

GITHUB_REPO = "playwright-api-test-temp"


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }

    request_context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers=headers,
    )

    yield request_context

    request_context.dispose()


@pytest.fixture(scope="session", autouse=True)
def create_test_repository(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:

    new_repo = api_request_context.post(
        "/user/repos",
        data={"name": GITHUB_REPO},
    )

    assert new_repo.ok, new_repo.text()

    yield

    deleted_repo = api_request_context.delete(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}"
    )

    assert deleted_repo.ok, deleted_repo.text()


def test_should_create_bug_report(
    api_request_context: APIRequestContext,
) -> None:

    data = {
        "title": "[Bug] report 1",
        "body": "Bug description",
    }

    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues",
        data=data,
    )

    assert new_issue.ok, new_issue.text()

    created_issue = new_issue.json()

    assert created_issue["title"] == "[Bug] report 1"
    assert created_issue["body"] == "Bug description"

    issue_number = created_issue["number"]

    issue = api_request_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues/{issue_number}"
    )

    assert issue.ok, issue.text()

    issue_response = issue.json()

    assert issue_response["title"] == "[Bug] report 1"
    assert issue_response["body"] == "Bug description"


def test_should_create_feature_request(
    api_request_context: APIRequestContext,
) -> None:

    data = {
        "title": "[Feature] request 1",
        "body": "Feature description",
    }

    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues",
        data=data,
    )

    assert new_issue.ok, new_issue.text()

    created_issue = new_issue.json()

    assert created_issue["title"] == "[Feature] request 1"
    assert created_issue["body"] == "Feature description"

    issue_number = created_issue["number"]

    issue = api_request_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues/{issue_number}"
    )

    assert issue.ok, issue.text()

    issue_response = issue.json()

    assert issue_response["title"] == "[Feature] request 1"
    assert issue_response["body"] == "Feature description"

# Код выполнен без ошибок. Результат - img/test_07.png