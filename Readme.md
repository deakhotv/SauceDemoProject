# 🧪 SauceDemo Automation Test Framework

A complete automation testing framework for SauceDemo website (https://www.saucedemo.com/) implementing all required test scenarios using Python, Selenium, and pytest.

## 📋 Test Scenarios Implemented

### ✅ Q1: Locked User Test [20 Marks]
- **Objective**: Verify locked user cannot login
- **Test**: Login with `locked_out_user` and verify error message
- **Validation**: "Epic sadface: Sorry, this user has been locked out."

### ✅ Q2: Standard User Test [50 Marks]
- **Objective**: Complete purchase journey
- **Test**: Login with `standard_user` → Reset app state → Add 3 items → Checkout → Verify success
- **Validation**: Product names, total price, and success message

### ✅ Q3: Performance User Test [30 Marks]
- **Objective**: Test with filtering and single item purchase
- **Test**: Login with `performance_glitch_user` → Reset app → Filter Z-A → Add first product → Checkout
- **Validation**: Product name, total price, and success message

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Chrome/Firefox Browser
- Git

### Installation & Execution

```bash
# Clone repository
git clone https://github.com/deakhotv/SauceDemoProject.git
cd SauceDemoProject

# Install dependencies
pip install -r requirements.txt

# Run complete test suite
python run_tests.py
