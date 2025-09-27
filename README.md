# 🧪 SauceDemo Automation Test Framework

Complete automation testing framework for SauceDemo website with support for individual and sequential test execution with Allure reports.

## 🎯 Execution Modes

### 1. Individual Test Execution
```bash
# Run Q1 only
pytest tests/test_q1_locked_user.py -v --alluredir=allure-results-q1

# Run Q2 only
pytest tests/test_q2_standard_user.py -v --alluredir=allure-results-q2

# Run Q3 only
pytest tests/test_q3_performance_user.py -v --alluredir=allure-results-q3
