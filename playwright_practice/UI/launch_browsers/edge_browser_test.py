# Tutorial: Launching Microsoft Edge Browser with Playwright
# -----------------------------------------------------------
# This script demonstrates how to launch Microsoft Edge using Playwright
# and perform a basic search on Google.
#
# Key Concepts:
#   - sync_playwright()               : Context manager that starts the Playwright engine (synchronous API).
#   - playwright.chromium.launch()    : Launches a Chromium-based browser. By passing the
#                                       channel="msedge" option, Playwright uses the installed
#                                       Microsoft Edge browser instead of bundled Chromium.
#                                       headless=False shows the visible browser window.
#   - browser.new_context()           : Creates an isolated browser context (like a new profile).
#   - context.new_page()              : Opens a new browser tab/page.
#   - page.set_viewport_size()        : Sets the browser window size (similar to maximize_window).
#   - page.goto(url)                  : Navigates to the specified URL.
#   - page.fill(selector, text)       : Fills an input field with the given text.
#   - page.click(selector)            : Clicks on a web element.
#   - page.wait_for_timeout(ms)       : Pauses execution for a given number of milliseconds.
#   - browser.close()                 : Closes the browser and ends the Playwright session.
#
# In this example, the script opens Google in Edge, searches for "Automation step by step",
# and clicks the search button, with short pauses to observe the actions.

import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto("https://google.com", wait_until="domcontentloaded")

    # Handle cookie consent button if it appears (common in some regions/environments)
    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
    except Exception:
        pass

    page.wait_for_selector("textarea[name='q'], input[name='q']", timeout=15000)

    page.fill("textarea[name='q'], input[name='q']", "Automation step by step")

    time.sleep(2)

    page.keyboard.press("Enter")

    time.sleep(2)

    browser.close()

print("Test Completed")
