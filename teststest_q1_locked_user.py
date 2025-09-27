import pytest
import allure
from pages.login_page import LoginPage
from utilities.config import Config

@allure.feature("Q1 - Locked User Test")
class TestLockedUser:
    @pytest.mark.order(1)
    @allure.title("Login with locked_out_user and verify error message")
    @allure.description("Test that locked_out_user cannot login and shows proper error message")
    def test_locked_user_login(self, driver):
        """Q1: Try login with locked_out_user and verify the error message."""
        with allure.step("Initialize login page"):
            login_page = LoginPage(driver)
        
        with allure.step(f"Login with locked user: {Config.LOCKED_USER}"):
            login_page.login(Config.LOCKED_USER, Config.PASSWORD)
        
        with allure.step("Verify error message"):
            error_message = login_page.get_error_message()
            expected_error = "Epic sadface: Sorry, this user has been locked out."
            
            allure.attach(f"Expected error: {expected_error}", name="Expected Error")
            allure.attach(f"Actual error: {error_message}", name="Actual Error")
            
            assert expected_error in error_message, f"Expected: {expected_error}, Got: {error_message}"
        
        with allure.step("Test completed successfully"):
            print(f"✓ Locked user test passed. Error message: {error_message}")