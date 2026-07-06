# Tutorial: Handling Alerts in Playwright
# ----------------------------------------
# This script demonstrates how to handle different types of JavaScript alerts
# in Playwright.
#
# Types of Alerts:
#   1. Simple Alert    : Displays a message with an "OK" button.
#   2. Confirm Alert   : Displays a message with "OK" and "Cancel" buttons.
#   3. Prompt Alert    : Displays a message with a text input field plus "OK" and "Cancel".
#
# Key Concepts for Alert Handling in Playwright:
#   - page.on("dialog", handler)         : Registers a listener for dialog events (alert/confirm/prompt).
#   - dialog.type                        : Returns the type of dialog: "alert", "confirm", or "prompt".
#   - dialog.message                     : Retrieves the message text displayed in the dialog.
#   - dialog.accept(prompt_text)         : Clicks the "OK" button; optionally types text for prompts.
#   - dialog.dismiss()                   : Clicks the "Cancel" button (dismisses the dialog).
#
# NOTE:
#   In Playwright, dialogs MUST be handled before they appear, by registering
#   a listener with page.on("dialog", ...) BEFORE triggering the action that opens the dialog.
#
# In this example, the script:
#   1. Triggers a simple alert on the Rediff login page by clicking sign in without credentials.
#   2. Navigates to a test page and handles a JS Alert, JS Confirm, and JS Prompt in sequence.

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ── 1. Simple Alert on Rediff Login ──────────────────────────────────────
        # Register a one-time listener BEFORE the click that triggers the alert.
        def handle_rediff_alert(dialog):
            print("Rediff Alert text:", dialog.message)
            dialog.accept()

        page.on("dialog", handle_rediff_alert)

        page.goto("https://mail.rediff.com/cgi-bin/login.cgi")
        page.locator("//button[normalize-space()='Log In']").click()
        page.wait_for_timeout(2000)

        # Remove the previous listener so it doesn't interfere with subsequent dialogs
        page.remove_listener("dialog", handle_rediff_alert)

        # ── 2. JS Alert ──────────────────────────────────────────────────────────
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        def handle_js_alert(dialog):
            print("JS Alert text:", dialog.message)
            dialog.accept()   # Click OK

        page.once("dialog", handle_js_alert)
        page.locator("//button[text()='Click for JS Alert']").click()
        page.wait_for_timeout(1000)

        # ── 3. JS Confirm ────────────────────────────────────────────────────────
        def handle_js_confirm(dialog):
            print("JS Confirm text:", dialog.message)
            dialog.dismiss()  # Click Cancel

        page.once("dialog", handle_js_confirm)
        page.locator("//button[text()='Click for JS Confirm']").click()
        page.wait_for_timeout(1000)

        # ── 4. JS Prompt ─────────────────────────────────────────────────────────
        def handle_js_prompt(dialog):
            print("JS Prompt text:", dialog.message)
            dialog.accept("Vishvambruth")  # Enter text and click OK

        page.once("dialog", handle_js_prompt)
        page.locator("//button[text()='Click for JS Prompt']").click()
        page.wait_for_timeout(2000)

        browser.close()


if __name__ == "__main__":
    main()

