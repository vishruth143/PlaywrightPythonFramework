# Tutorial: Handling Dropdowns in Playwright
# -------------------------------------------
# This script demonstrates how to interact with HTML <select> dropdown elements
# in Playwright using the select_option() method.
#
# Key Method:
#   - locator.select_option(...)  : Selects one or more options in a <select> element.
#
# Ways to Select Options:
#   - By visible text  : select_option(label="Option Text")
#   - By value attr    : select_option(value="option_value")
#   - By index         : select_option(index=2)
#   - Multi-select     : select_option(["Option1", "Option2"])  (pass a list of labels/values)
#
# Other Useful Methods:
#   - locator.inner_text()        : Get visible text of an element.
#   - page.locator("select option"): Locate all <option> elements inside a <select>.
#   - locator.all_inner_texts()   : Returns a list of visible text for all matched elements.
#
# In this example, the script:
#   1. Selects "ANTARCTICA" from a country dropdown by visible text and prints all available options.
#   2. Navigates to a multi-select dropdown and selects items by label and by index.

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ── 1. Single-Select Dropdown ─────────────────────────────────────────
        page.goto("https://demo.guru99.com/test/newtours/register.php")

        country_dropdown = page.locator("select[name='country']")

        # Select by visible text
        country_dropdown.select_option(label="ANTARCTICA")
        print("Selected: ANTARCTICA")

        # Get and print all available options
        all_options = page.locator("select[name='country'] option").all_inner_texts()
        print(f"Total countries: {len(all_options)}")
        for option in all_options:
            print(option)

        # ── 2. Multi-Select Dropdown ──────────────────────────────────────────
        page.goto("http://jsbin.com/osebed/2")

        fruits_dropdown = page.locator("#fruits")

        # Select by visible text
        fruits_dropdown.select_option(label="Banana")
        print("\nSelected: Banana")

        # Select by index (0-based: index 1 = second option)
        fruits_dropdown.select_option(index=1)
        print("Selected by index 1")

        page.wait_for_timeout(3000)

        browser.close()


if __name__ == "__main__":
    main()

