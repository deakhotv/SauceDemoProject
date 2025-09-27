from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from utilities.config import Config

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)
    
    def login(self, username, password):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)