from playwright.sync_api import Page, expect, ViewportSize


def test_ui_validation_dynamic_script(page:Page):
    # Add iphone X and Nokia Edge to the cart and validate 2 items in the cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button", name="Add").click()
    nokia_edge_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_edge_product.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

# Child Window Handle
def test_child_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").first.click()
    child_page = new_page_info.value
    child_page.wait_for_load_state()
    expect(child_page.locator("div[class='inner-box'] h1")).to_have_text("Documents request")
    expect(child_page.locator(".red").first).to_contain_text("mentor@rahulshettyacademy.com")
    text = child_page.locator(".red").first.text_content()
    print(text)
    # Extract the email from the text
    print(text.split("at ")[0])
    print(text.split("at ")[1])
    email = text.split("at ")[1].split(" ")[0]
    print(email)
    assert email == "mentor@rahulshettyacademy.com"
