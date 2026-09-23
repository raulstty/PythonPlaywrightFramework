# Python Playwright Test Automation Framework

[![Playwright Tests](https://github.com/raulstty/PythonPlaywrightFramework/actions/workflows/tests.yml/badge.svg)](https://github.com/raulstty/PythonPlaywrightFramework/actions/workflows/tests.yml)

A test automation framework built with **Playwright (Python)** and **pytest**, covering UI tests, API tests, and tests that combine both. It runs automatically on every push through GitHub Actions and publishes an HTML report.

## What it demonstrates

- **Page Object Model** with a shared `BasePage` (inheritance) that wraps Playwright's `Page` (composition)
- **API client layer** built on Playwright's `APIRequestContext`: a `BaseClient` plus one client class per resource
- **Combined API + UI tests**: the API is the source of truth, the UI is verified against it
- **Fixture-based setup/teardown** in `conftest.py` with deliberate scoping (session for the HTTP context, function for pages)
- **Data-driven tests** using `pytest.mark.parametrize` fed from a JSON file
- **Auto-retrying assertions** with `expect()` instead of one-shot `assert` on UI state
- **Cross-browser and parallel runs** (Chromium, Firefox, WebKit, `pytest-xdist`)
- **Reporting**: self-contained HTML report with screenshots on failure
- **CI**: GitHub Actions on a clean Ubuntu runner, report uploaded as an artifact

## Project structure

```
.
├── .github/workflows/tests.yml   # CI pipeline
├── api/
│   ├── base_client.py            # generic get/post over APIRequestContext
│   ├── posts_client.py           # /posts resource (jsonplaceholder)
│   └── rooms_client.py           # /api/room resource (automationintesting.online)
├── pages/
│   ├── base_page.py              # shared page behaviour
│   ├── login_page.py             # practicetestautomation.com login
│   └── rooms_page.py             # automationintesting.online home page
├── data/
│   └── login_test_data.json      # test data kept out of the test code
├── conftest.py                   # fixtures: pages, API clients, API context
├── pytest.ini                    # default pytest options
├── test_intro.py                 # UI tests
├── test_api.py                   # API tests
├── test_api_ui.py                # combined API + UI test
└── requirements.txt              # pinned dependencies
```

## Setup

Requires Python 3.14 (the version used in development and CI).

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

To run against all browsers, also run `playwright install firefox webkit`.

## Running the tests

```powershell
# everything
python -m pytest -v

# watch the browser
python -m pytest -v --headed --slowmo 1000

# in parallel
python -m pytest -v -n auto

# several browsers at once
python -m pytest -v --browser chromium --browser firefox --browser webkit

# with an HTML report
python -m pytest -v --html=reports/report.html --self-contained-html
```

The API base URL can be overridden with `--api-base-url`, and the UI base URL with `--base-url`.

## Design notes

- **Tests never touch locators or HTTP details.** UI interaction lives in page objects and HTTP details live in clients, so a UI or endpoint change is fixed in one place.
- **Isolation by default.** `page` is function-scoped, so each test gets its own browser context. That is also what makes parallel execution safe.
- **Base URL lives in `addopts`, not a `base_url` ini key.** `pytest-base-url` skips the ini value on `pytest-xdist` worker processes, so relative navigation failed under `-n`. Passing `--base-url` through `addopts` is parsed by pytest itself on every process and works in parallel runs.
- **Failure screenshots** are captured automatically (`--screenshot=only-on-failure`) and embedded in the HTML report.

## Practice sites used

| Purpose | Site |
|---|---|
| UI login tests | practicetestautomation.com |
| API tests | jsonplaceholder.typicode.com |
| API + UI tests | automationintesting.online |

These are public sites made for practising automation. Test data on them is shared and may reset.
