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
    context.dispose()          # clean up after all tests finish

# ── 1. GET Requests ─────────────────────────────────────────────────
def test_get_single_post(api: APIRequestContext):
    response = api.get("/posts/1")

    # 1. Check the status code
    assert response.status == 200

    # 2. Parse the JSON body into a Python dict
    body = response.json()
    # body == {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}

    # 3. Assert specific fields
    assert body["id"] == 1
    assert body["userId"] == 1
    assert "title" in body

def test_get_all_posts(api: APIRequestContext):
    response = api.get("/posts")

    assert response.ok
    assert response.status == 200
    posts = response.json()
    assert len(posts) == 100        # JSONPlaceholder has 100 posts
    assert posts[0]["id"] == 1

# ── 2. POST Requests ─────────────────────────────────────────────────
def test_create_post(api: APIRequestContext):
    new_post = {
        "title": "My First Post",
        "body":  "Hello from Playwright!",
        "userId": 1
    }

    response = api.post("/posts", data=new_post)

    assert response.status == 201    # 201 = Created
    body = response.json()
    assert body["title"] == "My First Post"
    assert "id" in body              # server assigned a new id
    print(f"Created post with id: {body['id']}")

# ── 3. PUT Requests ─────────────────────────────────────────────────
def test_update_post_put(api: APIRequestContext):
    updated = {
        "id": 1,
        "title": "Replaced Title",
        "body":  "Replaced body.",
        "userId": 1
    }

    response = api.put("/posts/1", data=updated)

    assert response.status == 200
    assert response.json()["title"] == "Replaced Title"

# ── 4. PATCH Requests ─────────────────────────────────────────────────
def test_update_post_patch(api: APIRequestContext):
    response = api.patch("/posts/1", data={"title": "Only title changed"})

    assert response.status == 200
    assert response.json()["title"] == "Only title changed"

# ── 5. DELETE Requests ─────────────────────────────────────────────────
def test_delete_post(api: APIRequestContext):
    response = api.delete("/posts/1")

    assert response.status == 200