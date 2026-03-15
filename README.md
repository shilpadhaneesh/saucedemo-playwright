# 🎭 Sauce Demo — Playwright Test Automation Framework

![Playwright Tests](https://github.com/YOUR_USERNAME/saucedemo-playwright/actions/workflows/playwright.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.44-green)
![pytest](https://img.shields.io/badge/pytest-9.0.2-orange)

A professional E2E test automation framework for [Sauce Demo](https://www.saucedemo.com) built with **Python 3.14**, **Playwright**, **pytest**, and **GitHub Actions CI/CD**.

---

## 📁 Project Structure

```
saucedemo-playwright/
├── pages/                        # Page Object Models (POM)
│   ├── login_page.py             # Login page interactions
│   ├── inventory_page.py         # Products/inventory page
│   ├── cart_page.py              # Shopping cart page
│   └── checkout_page.py         # Checkout flow
├── tests/                        # Test suites
│   ├── test_login.py             # 7 login tests
│   ├── test_inventory.py         # 9 inventory/sorting tests
│   └── test_checkout.py         # 9 checkout E2E tests
├── reports/                      # Auto-generated HTML reports
├── .github/workflows/
│   └── playwright.yml            # CI/CD — runs on push & daily schedule
├── conftest.py                   # Shared fixtures & config
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
└── .env.example                  # Environment variable template
```

---

## 🧪 Test Coverage (25 Test Cases)

| Module | Tests | Coverage |
|--------|-------|----------|
| Login | 7 | Valid login, locked user, wrong password, empty fields, error dismiss, logout |
| Inventory | 9 | Product count, add/remove items, cart badge, all 4 sort options |
| Checkout | 9 | Cart validation, form validation, full E2E flow, price check, order confirmation |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.14+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/saucedemo-playwright.git
cd saucedemo-playwright

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install chromium firefox

# 5. Copy environment file
copy .env.example .env         # Windows
cp .env.example .env           # Mac/Linux
```

### Running Tests

```bash
# Run all tests
pytest

# Run with visible browser
pytest --headless-mode=false

# Run specific test file
pytest tests/test_checkout.py -v

# Run in Firefox
pytest --browser=firefox

# Run smoke tests only
pytest -m smoke

# Run regression tests only
pytest -m regression

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🏗️ Design Patterns

### Page Object Model (POM)
Each page is a separate class with locators and user action methods for clean, maintainable tests.

### pytest Fixtures (conftest.py)
- Session-scoped browser config
- Shared `credentials` fixture for all tests
- Environment variables via `.env`

### CI/CD (GitHub Actions)
- Runs on every push to `main`/`develop`
- Parallel execution across Chromium and Firefox
- Daily scheduled run at 9am (Mon–Fri)
- HTML + Allure reports uploaded as build artifacts

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.14 | Core language |
| Playwright | 1.44 | Browser automation |
| pytest | 9.0.2 | Test runner |
| pytest-playwright | 0.5.0 | Playwright-pytest integration |
| pytest-html | 4.1.1 | HTML test reports |
| allure-pytest | 2.15.3 | Allure reporting |
| python-dotenv | 1.0.1 | Environment config |
| GitHub Actions | — | CI/CD pipeline |

---

## 👤 Author

*Shilpa Dhaneesh*
- LinkedIn: [linkedin.com/in/shilpa-rajappan](https://linkedin.com/in/shilpa-rajappan)
- GitHub: [@shilpadhaneesh](https://github.com/shilpadhaneesh)

---

*Portfolio project demonstrating QA automation skills.*
