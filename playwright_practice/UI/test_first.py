from playwright.sync_api import Page

def test_page_title(page: Page):
    page.goto("https://www.google.com")
    print(page.title())          # prints: Google
    assert "Google" in page.title()