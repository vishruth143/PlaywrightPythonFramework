from playwright.sync_api import Playwright

def test_api_get(playwright:Playwright):
    request_context = playwright.request.new_context(extra_http_headers={
        "Accept": "application/json"
    })
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status == 200
    assert "application/json" in response.headers["content-type"]

    data = response.json()
    print(data)
    assert data.get("userId") == 1
    assert data.get("id") == 1
    assert data["id"] == 1
    request_context.dispose()
