import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.exceptions_page import ExceptionPage


class TestException:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exception_no_such = ExceptionPage(driver)
        # Open page
        exception_no_such.open()

        # Click Add button
        exception_no_such.add_second_row()

        # Verify row2 input is displayed
        assert exception_no_such.is_row2_displayed, "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        exception_not_interactable = ExceptionPage(driver)
        # Open page
        exception_not_interactable.open()

        # Click Add button
        exception_not_interactable.add_second_row()

        # Verify row2 input is displayed
        assert exception_not_interactable.is_row2_displayed, "Row 2 input should be displayed, but it's not"

        # Type text into the second input field
        exception_not_interactable.add_row2_food("Shushi")

        # Verify confirmation message
        assert exception_not_interactable.get_confirmation_message == "Row 2 was saved", "Confirmation message is not correct"