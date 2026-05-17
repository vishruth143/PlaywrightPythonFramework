# Tutorial: Taking Screenshots in Playwright
# -------------------------------------------
# This script demonstrates how to capture and save screenshots of a web page
# using Playwright. Screenshots are useful for visual validation,
# debugging test failures, and generating test reports.
#
# Key Methods:
#   - page.screenshot(path=file_path)         : Captures the current viewport and saves it
#                                               as a PNG image to the given path.
#   - page.screenshot(path=..., full_page=True): Captures the FULL scrollable page (not just viewport).
#   - locator.screenshot(path=file_path)       : Captures only a specific element as a screenshot.
#
# Options for page.screenshot():
#   - path        : File path to save the screenshot (PNG or JPEG based on extension).
#   - full_page   : If True, captures the entire scrollable page. Default is False (viewport only).
#   - clip        : Dict with x, y, width, height to capture a specific region.
#   - type        : "png" (default) or "jpeg".
#   - quality     : JPEG quality (0-100), only applicable for JPEG.
#
# Best Practices:
#   - Use os.path.join() to build file paths in a cross-platform compatible way.
#   - Use os.makedirs(path, exist_ok=True) to ensure the output directory exists
#     before saving, without raising an error if it already exists.
#   - Wrap screenshot logic in a try/except block to handle errors gracefully.
#   - Organize screenshots into a dedicated folder (e.g., "screenshots/") for easy access.
#
# In this example, the script:
#   1. Launches Chromium and navigates to Google.
#   2. Calls a reusable take_screenshot() function that ensures the output
#      directory exists and saves:
#        a. A full-page screenshot.
#        b. A viewport-only screenshot.

import os

from playwright.sync_api import sync_playwright


def take_screenshot(page, file_name, full_page=False):
    """
    Captures a screenshot of the current page and saves it to the screenshots/ directory.

    :param page:      Playwright Page object.
    :param file_name: Base name for the screenshot file (without extension).
    :param full_page: If True, captures the entire scrollable page.
    """
    # Define screenshots directory relative to this script's location
    screenshots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
    # Create the directory if it doesn't exist
    os.makedirs(screenshots_dir, exist_ok=True)
    # Build the full file path
    file_path = os.path.join(screenshots_dir, f"{file_name}.png")
    # Take and save the screenshot
    page.screenshot(path=file_path, full_page=full_page)
    print(f"Screenshot saved: {file_path}")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com/")

        try:
            # Viewport screenshot (default)
            take_screenshot(page, "Google_HomePage_Viewport")

            # Full-page screenshot
            take_screenshot(page, "Google_HomePage_FullPage", full_page=True)

            print("All screenshots saved successfully!")
        except Exception as e:
            print(f"Failed to take screenshot: {str(e)}")

        browser.close()


if __name__ == "__main__":
    main()

