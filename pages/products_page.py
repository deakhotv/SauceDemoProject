from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SIDEBAR_MENU = (By.CLASS_NAME, "bm-menu-wrap")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    def open_menu(self):
        self.click(self.HAMBURGER_MENU)
        self.wait.until(EC.visibility_of_element_located(self.SIDEBAR_MENU))
    
    def reset_app_state(self):
        self.open_menu()
        self.click(self.RESET_APP_STATE)
        self.driver.refresh()
    
    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)
    
    def add_product_to_cart(self, index):
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
    
    def add_multiple_products_to_cart(self, indices):
        for index in indices:
            self.add_product_to_cart(index)
    
    def get_cart_count(self):
        if self.is_displayed(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0
    
    def go_to_cart(self):
        self.click(self.CART_LINK)
    
    def filter_products(self, filter_type):
        filter_dropdown = self.find_element(self.FILTER_DROPDOWN)
        select = Select(filter_dropdown)
        select.select_by_visible_text(filter_type)
    
    def get_product_names(self):
        return [element.text for element in self.find_elements(self.PRODUCT_NAMES)]
    
    def get_product_prices(self):
        return [float(element.text.replace('$', '')) for element in self.find_elements(self.PRODUCT_PRICES)]