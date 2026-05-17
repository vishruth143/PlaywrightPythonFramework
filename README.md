# 🎭 Playwright Python Framework

> **Enterprise-grade browser automation and API testing framework** built with [Microsoft Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org/), written in Python 3.

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.59.0-green?logo=microsoftedge)](https://playwright.dev/python/)
[![pytest](https://img.shields.io/badge/pytest-9.x-orange?logo=pytest)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running Tests](#running-tests)
- [Module Documentation](#module-documentation)
  - [playwright\_practice (Core Tests)](#playwright_practice-core-tests)
  - [launch\_browsers](#launch_browsers)
  - [handle\_alert](#handle_alert)
  - [handle\_dropdown](#handle_dropdown)
  - [handle\_popup](#handle_popup)
  - [iframe](#iframe)
  - [takescreenshot](#takescreenshot)
- [Playwright vs Selenium — Key Differences](#playwright-vs-selenium--key-differences)
- [Best Practices](#best-practices)
- [CI/CD Integration](#cicd-integration)
- [Contributing](#contributing)

---

## Overview

This framework demonstrates **professional browser automation** techniques using Playwright's Python API. It covers all major web automation challenges encountered in enterprise QA environments:

| Capability | Description |
|---|---|
| 🌐 **Cross-Browser Testing** | Chrome, Firefox, Microsoft Edge |
| 🚨 **Alert Handling** | Simple alerts, confirms, and prompts |
| 📋 **Dropdown Handling** | Single-select and multi-select `<select>` elements |
| 🪟 **Popup / New Tab Handling** | Context-level new page/tab capturing |
| 🖼️ **iFrame Handling** | Scoped frame locators without switching |
| 📸 **Screenshots** | Viewport and full-page screenshot capture |
| 🔌 **API Testing** | HTTP request context with assertions |
| ✅ **UI Validations** | Assertions using Playwright's `expect` API |

---

## Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.13 | Programming language |
| Playwright | 1.59.0 | Browser automation engine |
| pytest | 9.x | Test runner & reporting |
| pytest-playwright | 0.7.2 | Playwright–pytest integration plugin |

---

## Project Structure

```
PlaywrightPythonFramework/
│
├── playwright_practice/                    # All automation scripts & tests
│   │
│   ├── test_playwright_basics.py           # Core Playwright fixture & locator tests
│   ├── test_ui_validations.py              # UI validations, cart & child window tests
│   ├── test_api_get.py                     # API testing using Playwright request context
│   │
│   ├── launch_browsers/                    # Browser launch demonstrations
│   │   ├── chrome_browser_test.py          # Launch & interact with Google Chrome
│   │   ├── edge_browser_test.py            # Launch & interact with Microsoft Edge
│   │   └── firefox_browser_test.py         # Launch & interact with Mozilla Firefox
│   │
│   ├── handle_alert/
│   │   └── alert_handle.py                 # Simple alert, JS Confirm & JS Prompt handling
│   │
│   ├── handle_dropdown/
│   │   └── handle_drop_down.py             # Single-select and multi-select dropdowns
│   │
│   ├── handle_popup/
│   │   └── popup_handle.py                 # New window / tab popup handling
│   │
│   ├── iframe/
│   │   └── iframe_handling.py              # iFrame interaction via frame_locator()
│   │
│   └── takescreenshot/
│       ├── screen_shot_handle.py           # Viewport & full-page screenshot capture
│       └── screenshots/                    # Auto-generated screenshot output folder
│
├── requirements.txt                        # Python package dependencies
├── .gitignore                              # Git ignore rules
└── README.md                              # This file
```

---

## Prerequisites

Ensure the following are installed on your machine before proceeding:

- ✅ [Python 3.10+](https://www.python.org/downloads/) (3.13 recommended)
- ✅ [pip](https://pip.pypa.io/en/stable/)
- ✅ [Git](https://git-scm.com/)
- ✅ [PyCharm](https://www.jetbrains.com/pycharm/) or any Python IDE (optional, recommended)

> **Note:** Playwright manages its own browser binaries. No ChromeDriver, GeckoDriver, or EdgeDriver installation is needed.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/PlaywrightPythonFramework.git
cd PlaywrightPythonFramework
```

### 2. Create & Activate Virtual Environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browser Binaries

```bash
playwright install
```

> This downloads Chromium, Firefox, and WebKit browser binaries managed by Playwright.

### 5. Configure PyCharm (Optional)

To set **pytest** as the default test runner in PyCharm:

1. Open `File` → `Settings` → `Tools` → `Python Integrated Tools`
2. Under **Testing**, set **Default test runner** to `pytest`
3. Click **Apply** → **OK**

---

## Running Tests

### Run All Tests

```bash
pytest playwright_practice/ -v
```

### Run a Specific Test File

```bash
pytest playwright_practice/test_playwright_basics.py -v
```

### Run a Specific Test Function

```bash
pytest playwright_practice/test_playwright_basics.py::test_core_locators -v
```

### Run Tests in Headed Mode (Visible Browser)

```bash
pytest playwright_practice/ --headed -v
```

### Run Tests on a Specific Browser

```bash
# Chromium (default)
pytest playwright_practice/ --browser chromium -v

# Firefox
pytest playwright_practice/ --browser firefox -v

# Microsoft Edge
pytest playwright_practice/ --browser msedge -v
```

### Run Tests with HTML Report

```bash
pytest playwright_practice/ -v --html=reports/report.html --self-contained-html
```

> Install `pytest-html` first: `pip install pytest-html`

### Run Standalone Scripts (Non-pytest)

```bash
python playwright_practice/handle_alert/alert_handle.py
python playwright_practice/handle_dropdown/handle_drop_down.py
python playwright_practice/handle_popup/popup_handle.py
python playwright_practice/iframe/iframe_handling.py
python playwright_practice/takescreenshot/screen_shot_handle.py
```

---

## Module Documentation

### `playwright_practice` (Core Tests)

| File | Description |
|---|---|
| `test_playwright_basics.py` | Demonstrates `playwright` and `page` fixtures, CSS/XPath locators, `get_by_*` APIs, multi-browser support |
| `test_ui_validations.py` | Cart interaction with `expect` assertions, child window (popup) handling |
| `test_api_get.py` | REST API GET request using Playwright's `request.new_context()`, JSON response validation |

---

### `launch_browsers`

Demonstrates how to launch and interact with different browsers using Playwright's synchronous API.

| File | Browser | Key API |
|---|---|---|
| `chrome_browser_test.py` | Google Chrome (Chromium) | `playwright.chromium.launch()` |
| `edge_browser_test.py` | Microsoft Edge | `playwright.chromium.launch(channel="msedge")` |
| `firefox_browser_test.py` | Mozilla Firefox | `playwright.firefox.launch()` |

---

### `handle_alert`

**File:** `handle_alert/alert_handle.py`

Handles all JavaScript dialog types in Playwright.

| Dialog Type | Playwright API | Action |
|---|---|---|
| Simple Alert | `page.on("dialog", handler)` | `dialog.accept()` |
| JS Confirm | `page.once("dialog", handler)` | `dialog.dismiss()` |
| JS Prompt | `page.once("dialog", handler)` | `dialog.accept("text")` |

> ⚠️ **Critical:** In Playwright, dialog handlers must be registered **before** the action that triggers the dialog.

---

### `handle_dropdown`

**File:** `handle_dropdown/handle_drop_down.py`

Handles HTML `<select>` dropdowns using Playwright's `select_option()` method.

| Selection Method | Playwright API |
|---|---|
| By visible text | `locator.select_option(label="Option Text")` |
| By value attribute | `locator.select_option(value="option_value")` |
| By index | `locator.select_option(index=2)` |
| Multi-select | `locator.select_option(["Label1", "Label2"])` |

---

### `handle_popup`

**File:** `handle_popup/popup_handle.py`

Handles new browser windows/tabs opened by user interactions.

```python
# Playwright approach — context manager captures the new page atomically
with context.expect_page() as new_page_info:
    page.get_by_text("Click Here").click()

popup_page = new_page_info.value
popup_page.wait_for_load_state("domcontentloaded")
```

---

### `iframe`

**File:** `iframe/iframe_handling.py`

Interacts with elements inside HTML iFrames using `frame_locator()` — no context switching required.

```python
# Playwright approach — scope all locators inside the iframe
iframe = page.frame_locator("//iframe[@id='iframeResult']")
iframe.locator("//button[@onclick='myFunction()']").click()
```

---

### `takescreenshot`

**File:** `takescreenshot/screen_shot_handle.py`

Captures screenshots for visual validation, debugging, and reporting.

| Screenshot Type | Playwright API |
|---|---|
| Viewport only (default) | `page.screenshot(path="shot.png")` |
| Full scrollable page | `page.screenshot(path="shot.png", full_page=True)` |
| Specific element only | `locator.screenshot(path="element.png")` |
| JPEG format | `page.screenshot(path="shot.jpg", type="jpeg", quality=80)` |

Screenshots are saved to: `playwright_practice/takescreenshot/screenshots/`

---

## Playwright vs Selenium — Key Differences

| Feature | Selenium | Playwright |
|---|---|---|
| **Alert Handling** | `driver.switch_to.alert` + `alert.accept()` | `page.on("dialog", handler)` — register BEFORE trigger |
| **Dropdown Selection** | `Select(el).select_by_visible_text()` | `locator.select_option(label="...")` |
| **New Tab / Popup** | `driver.window_handles` + `switch_to.window()` | `context.expect_page()` — context manager |
| **iFrame Handling** | `driver.switch_to.frame(el)` — must switch in/out | `page.frame_locator(selector)` — no switching needed |
| **Screenshots** | `driver.save_screenshot(path)` — viewport only | `page.screenshot(full_page=True/False)` — supports full page |
| **API Testing** | Requires external library (e.g., `requests`) | Built-in `playwright.request.new_context()` |
| **Waits** | Explicit/Implicit `WebDriverWait` | Auto-waiting — no explicit waits needed in most cases |
| **Browser Drivers** | ChromeDriver / GeckoDriver required | No drivers — Playwright manages binaries |
| **Multi-browser** | Separate drivers per browser | `playwright.chromium / firefox / webkit` |

---

## Best Practices

### ✅ Do

- Use `page.once("dialog", handler)` for one-time dialog handling to avoid listener leaks
- Use `context.expect_page()` **before** the click that opens a new tab
- Use `page.frame_locator()` instead of switching into/out of frames
- Use `page.screenshot(full_page=True)` for complete page capture in failure reports
- Use `os.path.join()` for cross-platform compatible screenshot paths
- Use `os.makedirs(path, exist_ok=True)` to safely create output directories
- Prefer `get_by_role()`, `get_by_label()`, `get_by_text()` over brittle XPath selectors
- Use Playwright's built-in `expect()` assertions — they auto-retry with timeout

### ❌ Avoid

- `time.sleep()` — prefer `page.wait_for_timeout()` or Playwright's auto-waiting
- `page.on("dialog")` for one-time use — use `page.once("dialog")` instead
- Hard-coded absolute file paths — use `os.path` utilities
- Registering dialog listeners after the action that triggers the dialog

---

## CI/CD Integration

### GitHub Actions Example

```yaml
# .github/workflows/playwright.yml
name: Playwright Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Install Playwright browsers
        run: playwright install --with-deps

      - name: Run Playwright tests
        run: pytest playwright_practice/ -v --html=reports/report.html --self-contained-html

      - name: Upload test report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report
          path: reports/
          retention-days: 30
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Usage |
|---|---|
| `feat:` | New feature or script |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `refactor:` | Code refactor without behaviour change |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks (deps, config) |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **Maintained by:** QA Automation Team  
> **Last Updated:** May 2026
