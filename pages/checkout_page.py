from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    # Locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    
    def fill_checkout_info(self, first_name="Test", last_name="User", postal_code="12345"):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)
    
    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
    
    def get_checkout_item_names(self):
        return [element.text for element in self.find_elements(self.ITEM_NAMES)]
    
    def get_item_total(self):
        text = self.get_text(self.ITEM_TOTAL)
        return float(text.replace('Item total: $', ''))
    
    def get_total_price(self):
        text = self.get_text(self.TOTAL)
        return float(text.replace('Total: $', ''))
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)