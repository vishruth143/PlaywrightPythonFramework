# Tutorial: Handling iFrames in Playwright
# ------------------------------------------
# An iFrame (Inline Frame) is an HTML element that embeds another HTML document
# within the current page. Playwright provides a clean API to locate and interact
# with elements inside iFrames without needing to "switch" focus like in Selenium.
#
# Key Methods:
#   - page.frame_locator(selector)          : Returns a FrameLocator for the specified iframe selector.
#                                             All further locators are scoped inside that iframe.
#   - frame_locator.locator(selector)       : Locates an element inside the iframe.
#   - page.frame(name=...)                  : Locates a frame by its name attribute.
#   - page.frames                           : Returns a list of all frames on the page.
#
# Ways to Locate an iFrame:
#   - By CSS selector  : page.frame_locator("iframe#iframeResult")
#   - By XPath         : page.frame_locator("//iframe[@id='iframeResult']")
#   - By name/id       : page.frame_locator("[name='iframeResult']")
#
# NOTE:
#   Unlike Selenium, Playwright does NOT require switching in/out of frames.
#   You simply scope your locator using frame_locator() and interact directly.
#   Dialogs (alerts/confirms/prompts) triggered inside an iframe are still
#   handled on the main `page` object using page.on("dialog", ...).
#
# In this example, the script:
#   1. Navigates to a W3Schools page containing an iFrame.
#   2. Locates and interacts with a button inside the iFrame using frame_locator().
#   3. Handles the JS Confirm alert triggered by that button click.

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm")

        # ── Register dialog handler BEFORE the click that triggers the alert ──
        def handle_confirm_dialog(dialog):
            print("Dialog type :", dialog.type)
            print("Dialog text :", dialog.message)
            dialog.dismiss()   # Click Cancel

        page.on("dialog", handle_confirm_dialog)

        # ── Locate the iframe and the button inside it ────────────────────────
        iframe = page.frame_locator("//iframe[@id='iframeResult']")

        # Click the button inside the iframe
        iframe.locator("//button[@onclick='myFunction()']").click()

        page.wait_for_timeout(2000)
        browser.close()


if __name__ == "__main__":
    main()

