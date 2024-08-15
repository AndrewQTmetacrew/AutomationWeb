import time

import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage


class TestNegativeScenario:
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, error_message):
        login_page = LoginPage(driver)
        # Open page
        login_page.open()

        # Type username incorrectUser into Username field
        login_page.execute_login(username, password)

        # Verify error message text is Your username is invalid!
        assert login_page.error_message_text == error_message, "Error message is not correct"