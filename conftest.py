import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.config import Config

@pytest.fixture
def driver():
    """Setup and teardown for WebDriver"""
    # Setup
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
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
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
                
                page_source = driver.page_source
                allure.attach(page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            except:
                pass