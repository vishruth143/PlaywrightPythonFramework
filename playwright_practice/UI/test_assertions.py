from playwright.sync_api import Page, expect

class TestAssertions:

    # ── 1. Page-level assertions ─────────────────────────────────────────────────
    def test_page_assertions(self, page: Page):
        page.goto("https://example.com")

        expect(page).to_have_title("Example Domain")
        expect(page).to_have_url("https://example.com/")

    # ── 2. Element visibility & text assertions ──────────────────────────────────
    def test_element_visibility_and_text(self, page: Page):
        page.goto("https://example.com")

        h1 = page.locator("h1")
        expect(h1).to_be_visible()
        expect(h1).to_have_text("Example Domain")

        # The paragraph below the heading contains a link – assert it exists
        learn_more_link = page.locator("a", has_text="Learn more")
        expect(learn_more_link).to_be_visible()
        expect(learn_more_link).to_have_attribute("href", "https://iana.org/domains/example")
        # The link should have a pointer cursor on hover
        expect(learn_more_link).to_have_css("cursor", "pointer")

    # ── 3. Checkbox assertions ───────────────────────────────────────────────────
    def test_checkbox_assertions(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/checkboxes")

        checkboxes = page.locator("input[type='checkbox']")

        # The page has two checkboxes; the second one is checked by default
        expect(checkboxes.nth(0)).not_to_be_checked()
        expect(checkboxes.nth(1)).to_be_checked()

        # Check the first one and verify
        checkboxes.nth(0).check()
        expect(checkboxes.nth(0)).to_be_checked()

    # ── 4. Input field – enabled state & value assertions ────────────────────────
    def test_input_assertions(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/login")

        username_input = page.locator("#username")
        password_input = page.locator("#password")
        login_button   = page.locator("button[type='submit']")

        # Fields and button must be visible and enabled
        expect(username_input).to_be_visible()
        expect(username_input).to_be_enabled()
        expect(password_input).to_be_enabled()
        expect(login_button).to_be_enabled()

        # Fill credentials and assert the typed value
        username_input.fill("tomsmith")
        password_input.fill("SuperSecretPassword!")
        expect(username_input).to_have_value("tomsmith")
        expect(password_input).to_have_value("SuperSecretPassword!")

    # ── 5. Success / error message & hidden element assertions ───────────────────
    def test_flash_message_assertions(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/login")

        # Successful login → flash message contains "You logged into..."
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()

        flash = page.locator("#flash")
        expect(flash).to_be_visible()
        expect(flash).to_contain_text("You logged into a secure area!")

        # The login form is no longer on the page
        expect(page.locator("#login")).to_be_hidden()

    # ── 6. Dynamic element – wait for visibility then hidden ─────────────────────
    def test_dynamic_loading_assertions(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        start_button = page.locator("#start button")
        loading_bar  = page.locator("#loading")
        finish_text  = page.locator("#finish")

        # Before clicking – finish text is hidden, loading bar is hidden
        expect(finish_text).to_be_hidden()

        start_button.click()

        # Loading bar appears while processing
        expect(loading_bar).to_be_visible()

        # After loading completes – finish text appears, loading bar disappears
        expect(finish_text).to_be_visible(timeout=10_000)
        expect(finish_text).to_have_text("Hello World!")
        expect(loading_bar).to_be_hidden()
