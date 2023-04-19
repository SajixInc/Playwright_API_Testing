from playwright.sync_api import APIRequestContext,Playwright
from typing import Generator
import pytest


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
)-> Generator[APIRequestContext,None,None]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


def test_post_example(api_request_context: APIRequestContext) -> None:
    headers = {"Content-type": "application/json"}
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    post_todo = api_request_context.post(
        f"https://jsonplaceholder.typicode.com/posts", data=data, headers=headers
    )
    # assert post_todo.ok
    assert post_todo.json()["title"] == "foo"


def test_get_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    get_todo = api_request_context.get(
        f"https://jsonplaceholder.typicode.com/posts/1",  headers=headers
    )
    assert get_todo.ok


def test_put_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    data = {
        "title": "foo2",
        "body": "bar",
        "userId": 1
    }
    put_todo = api_request_context.put(
        f"https://jsonplaceholder.typicode.com/posts/1", data=data, headers=headers
    )
    assert put_todo.ok
    assert put_todo.status == 200
    assert put_todo.json()["title"] == "foo2"


def test_delete_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    delete_todo = api_request_context.delete(
        f"https://jsonplaceholder.typicode.com/posts/1", headers=headers)
    assert delete_todo.ok
    assert delete_todo.status == 200
