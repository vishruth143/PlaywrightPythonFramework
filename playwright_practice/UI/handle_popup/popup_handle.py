# Tutorial: Handling Popup Windows in Playwright
# ------------------------------------------------
# This script demonstrates how to handle browser popup windows (new tabs/windows)
# that open when interacting with web elements in Playwright.
#
# Key Concepts:
#   - browser_context.expect_page()  : Context manager that waits for a new page/tab to open.
#   - page.wait_for_load_state()     : Waits until the page reaches a specific load state.
#   - page.title()                   : Returns the title of the current page.
#   - page.close()                   : Closes the current page/tab.
#
# Typical Workflow for Handling Popups in Playwright:
#   1. Use `with context.expect_page() as new_page_info:` BEFORE clicking the element.
#   2. Perform the click inside the `with` block to trigger the popup.
#   3. Retrieve the new page with `new_page_info.value` after the block.
#   4. Wait for the new page to finish loading.
#   5. Perform actions on the popup page.
#   6. Close the popup and continue on the main page.
#
# NOTE:
#   Unlike Selenium, Playwright uses a context-based approach for new windows/tabs,
#   making it more reliable and avoiding race conditions.
#
# In this example, the script opens a new window via a link click, reads its title
# and content, closes it, and then continues on the main window.

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Create a browser context (all tabs/windows share the same context)
        context = browser.new_context()
        page = context.new_page()

        # ── Step 1: Open the main page ────────────────────────────────────────
        page.goto("https://the-internet.herokuapp.com/windows")
        print("Main Window Title:", page.title())

        # ── Step 2 & 3: Click link and capture the new popup page ─────────────
        # expect_page() listens for a new page BEFORE the click triggers it
        with context.expect_page() as new_page_info:
            page.get_by_text("Click Here").click()

        popup_page = new_page_info.value

        # ── Step 4: Wait for the popup to finish loading ──────────────────────
        popup_page.wait_for_load_state("domcontentloaded")

        # ── Step 5: Interact with the popup window ────────────────────────────
        print("Popup Window Title:", popup_page.title())
        print("Popup Window Text:", popup_page.locator("h3").inner_text())

        # ── Step 6: Close the popup and verify main window ────────────────────
        popup_page.close()

        print("Back to Main Window:", page.title())

        page.wait_for_timeout(2000)
        browser.close()


if __name__ == "__main__":
    main()

