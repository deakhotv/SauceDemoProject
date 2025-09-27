from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def send_keys(self, locator, text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)
    
    def get_text(self, locator):
        return self.find_element(locator).text
    
    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False