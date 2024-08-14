import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenario:
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, error_message):
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        submit_btn = driver.find_element(By.ID, "submit")
        submit_btn.click()
        time.sleep(0.1)
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Message was not displayed"
        assert error_message_locator.text == error_message, "Error message is not correct"
