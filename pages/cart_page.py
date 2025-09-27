from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def get_cart_items_count(self):
        return len(self.find_elements(self.CART_ITEMS))
    
    def get_cart_item_names(self):
        return [element.text for element in self.find_elements(self.ITEM_NAMES)]
    
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)