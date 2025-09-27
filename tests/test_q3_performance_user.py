import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.config import Config

@allure.feature("Q3 - Performance User Test")
class TestPerformanceUser:
    @pytest.mark.order(3)
    @allure.title("Complete purchase journey with performance_glitch_user")
    @allure.description("Login, reset app, filter Z-A, add first product, checkout, verify success, logout")
    def test_performance_user_flow(self, driver):
        """Q3: Complete purchase journey with performance_glitch_user"""
        with allure.step("Login with performance_glitch_user"):
            login_page = LoginPage(driver)
            login_page.login(Config.PERFORMANCE_USER, Config.PASSWORD)
        
        with allure.step("Initialize products page and reset app state"):
            products_page = ProductsPage(driver)
            products_page.reset_app_state()
        
        with allure.step("Filter products by Name (Z to A)"):
            products_page.filter_products("Name (Z to A)")
            
            product_names = products_page.get_product_names()
            allure.attach(f"Products after Z-A filter: {product_names}", name="Filtered Products")
        
        with allure.step("Add first product to cart (last alphabetically)"):
            products_page.add_product_to_cart(0)
            
            cart_count = products_page.get_cart_count()
            allure.attach(f"Cart count: {cart_count}", name="Cart Count")
            assert cart_count == 1, "Cart should have 1 item"
        
        with allure.step("Navigate to cart and verify item"):
            products_page.go_to_cart()
            cart_page = CartPage(driver)
            
            cart_items_count = cart_page.get_cart_items_count()
            cart_item_names = cart_page.get_cart_item_names()
            
            allure.attach(f"Cart items count: {cart_items_count}", name="Cart Items Count")
            allure.attach(f"Product in cart: {cart_item_names}", name="Cart Product")
            
            assert cart_items_count == 1, "Cart should have 1 item"
        
        with allure.step("Proceed to checkout"):
            cart_page.proceed_to_checkout()
        
        with allure.step("Fill checkout information"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_info()
        
        with allure.step("Verify product name and total price"):
            checkout_product_names = checkout_page.get_checkout_item_names()
            total_price = checkout_page.get_total_price()
            
            allure.attach(f"Product in checkout: {checkout_product_names}", name="Checkout Product")
            allure.attach(f"Total price: ${total_price}", name="Total Price")
            
            assert len(checkout_product_names) == 1, "Should have 1 product in checkout"
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
            print("✓ Performance user test completed successfully")