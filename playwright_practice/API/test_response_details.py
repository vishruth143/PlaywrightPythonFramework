import pytest
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator

@pytest.fixture(scope="session")
def api(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """One HTTP session shared by all tests in this file."""
    context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield context
    context.dispose()

def test_response_details(api: APIRequestContext):
    response = api.get("/posts/1")

    # ── Status ─────────────────────────────────────────────
    assert response.status == 200
    assert response.ok                    # True for any 2xx code

    # ── Headers ────────────────────────────────────────────
    headers = dict(response.headers)
    assert "content-type" in headers
    assert "application/json" in headers["content-type"]

    # ── JSON body ──────────────────────────────────────────
    body = response.json()
    assert isinstance(body, dict)         # a single object, not a list
    assert body["id"] == 1

    # ── Raw text body ──────────────────────────────────────
    text = response.text()
    assert "\"id\": 1" in text