
# PyQA Nexus

### Python Playwright Test Automation Framework

PyQA Nexus is a Python-based UI automation framework
developed using Playwright, Pytest, and the Page Object
Model (POM) design pattern.

The project automates key user workflows of the
SauceDemo e-commerce application.

## Tech Stack

- Python 3.13
- Playwright
- Pytest
- Page Object Model (POM)
- pytest-html
- Microsoft Edge

## Application Under Test

https://www.saucedemo.com/

## Test Coverage

| Test ID | Test Scenario | Type |
|---------|---------------|------|
| TC001 | Valid Login | Positive |
| TC002 | Invalid Login | Negative |
| TC003 | Products Verification | Positive |
| TC004 | Add Product to Cart | Positive |
| TC005 | Remove Product from Cart | Positive |

## Project Structure

```text
pyqa-nexus/
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   └── test_cart.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/pyqa-nexus.git

Navigate to the project:

    cd pyqa-nexus

Create virtual environment:

    python -m venv .venv

Activate virtual environment (PowerShell):

    .venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

Install Playwright Chromium:

    python -m playwright install chromium

## Test Execution

Run all tests:

    python -m pytest tests/ -v

Run with Microsoft Edge:

    python -m pytest tests/ --browser-channel msedge --headed -v

## HTML Reporting

Generate HTML report:

    python -m pytest tests/ --browser-channel msedge -v --html=report.html --self-contained-html

Open report:

    start report.html

## Current Execution Results

- Total Tests: 5
- Passed: 5
- Failed: 0
- Pass Rate: 100%

## Future Enhancements

- Additional test scenarios
- Data-driven testing
- Allure reporting
- Cross-browser execution
- GitHub Actions CI/CD integration

## Author

Nilavarasi Raj
