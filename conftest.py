import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.config import Config

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

@pytest.fixture
def driver(request):
    """Setup and teardown for WebDriver"""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    # Setup
    if browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
    else:  # chrome
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    
    if browser.lower() == "firefox":
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )
    else:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    yield driver
    
    # Teardown
    if driver:
        driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to add screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                # Take screenshot
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
                
                # Add page source
                page_source = driver.page_source
                allure.attach(page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
                
                # Add browser logs
                logs = driver.get_log('browser')
                if logs:
                    allure.attach(str(logs), name="browser_logs", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                print(f"Failed to capture failure details: {e}")