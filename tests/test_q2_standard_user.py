import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.config import Config

@allure.feature("Q2 - Standard User Test")
class TestStandardUser:
    @pytest.mark.order(2)
    @allure.title("Complete purchase journey with standard_user")
    @allure.description("Login, reset app, add 3 items, checkout, verify success, logout")
    def test_standard_user_flow(self, driver):
        """Q2: Complete purchase journey with standard_user"""
        with allure.step("Login with standard_user"):
            login_page = LoginPage(driver)
            login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        
        with allure.step("Initialize products page and reset app state"):
            products_page = ProductsPage(driver)
            products_page.reset_app_state()
        
        with allure.step("Add three items to cart"):
            products_page.add_multiple_products_to_cart([0, 1, 2])
            
            cart_count = products_page.get_cart_count()
            allure.attach(f"Cart count after adding items: {cart_count}", name="Cart Count")
            assert cart_count == 3, "Cart should have 3 items"
        
        with allure.step("Navigate to cart and verify items"):
            products_page.go_to_cart()
            cart_page = CartPage(driver)
            
            cart_items_count = cart_page.get_cart_items_count()
            assert cart_items_count == 3, "Cart should have 3 items"
        
        with allure.step("Proceed to checkout"):
            cart_page.proceed_to_checkout()
        
        with allure.step("Fill checkout information"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_info()
        
        with allure.step("Verify product names and total price"):
            product_names = checkout_page.get_checkout_item_names()
            total_price = checkout_page.get_total_price()
            
            allure.attach(f"Products: {product_names}", name="Products in Checkout")
            allure.attach(f"Total price: ${total_price}", name="Total Price")
            
            assert len(product_names) == 3, "Should have 3 products in checkout"
            assert total_price > 0, "Total price should be greater than 0"
        
        with allure.step("Finish purchase and verify success message"):
            checkout_page.finish_checkout()
            
            success_message = checkout_page.get_success_message()
            expected_message = "Thank you for your order!"
            
            allure.attach(f"Expected: {expected_message}", name="Expected Message")
            allure.attach(f"Actual: {success_message}", name="Actual Message")
            
            assert expected_message in success_message, f"Expected: {expected_message}, Got: {success_message}"
        
        with allure.step("Reset app state and logout"):
            products_page.reset_app_state()
            products_page.logout()
        
        with allure.step("Test completed successfully"):
            print("✓ Standard user test completed successfully")