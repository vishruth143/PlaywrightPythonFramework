from playwright.sync_api import Page, expect, ViewportSize
from playwright.sync_api import Playwright


# playwrite:Playwrite Fixture
def test_playwright_fixture(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport=ViewportSize(width=1920, height=1080))
    try:
        page = context.new_page()
        page.goto("https://www.google.com", wait_until="domcontentloaded")
        title = page.title()
        assert "Google" in title, f"Actual title: {title}"
    finally:
        context.close()
        browser.close()

# Page fixture by default have chromium with headless mode and 1 single context
def test_playwright_page_fixture(page:Page):
    try:
        page.goto("https://www.google.com", wait_until="domcontentloaded")
        title = page.title()
        assert "Google" in title, f"Actual title: {title}"
    finally:
        page.close()

'''
# CSS Locators:
-------------------------------------------------------------------------------------
    Attribute                       |   Locator Syntax          |   Example         |
-------------------------------------------------------------------------------------
    id                              |   #idname                 |   #username       |
                                    |   tagname#idname          |   input#username  |
    classname                       |   .classname              |   .search-keyword |
                                    |   tagname.classname       |   button.submit   |
    Customized with any attribute   |   tagname[attribute=value]|   input[type=text]|
    tagnames                        |   form input              |   form input      |
-------------------------------------------------------------------------------------
'''

# Core Locators
def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

# Invalid Login
def test_invalid_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("test1234")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

# Firefox Browser
def test_playwright_firefox(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(viewport=ViewportSize(width=1920, height=1080))
    try:
        page = context.new_page()
        page.goto("https://www.google.com", wait_until="domcontentloaded")
        title = page.title()
        assert "Google" in title, f"Actual title: {title}"
    finally:
        context.close()
        browser.close()
