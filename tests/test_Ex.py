import pytest
from page_objects.exceptions_page import ExceptionPage


class TestException:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exception_no_such = ExceptionPage(driver)
        exception_no_such.open()
        exception_no_such.add_second_row()
        assert exception_no_such.is_row2_displayed, "Row 2 input should be displayed, but it's not"
    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exception_not_interactable = ExceptionPage(driver)
        exception_not_interactable.open()
        exception_not_interactable.add_second_row()
        assert exception_not_interactable.is_row2_displayed, "Row 2 input should be displayed, but it's not"
        exception_not_interactable.add_row2_food("Shushi")
        assert exception_not_interactable.get_confirmation_message == "Row 2 was saved", "Confirmation message is not correct"
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exception_invalid_state = ExceptionPage(driver)
        exception_invalid_state.open()
        exception_invalid_state.modify_row1_input("Bugger")
        assert exception_invalid_state.get_confirmation_message == "Row 1 was saved", "Confirmation message is not correct"
    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exception_stale_reference = ExceptionPage(driver)
        exception_stale_reference.open()
        exception_stale_reference.add_second_row()
        assert not exception_stale_reference.is_instructions_displayed , "Instructions is displayed"
    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exception_timeout = ExceptionPage(driver)
        exception_timeout.open()
        exception_timeout.add_second_row()
        assert exception_timeout.is_row2_displayed, "Row 2 input should be displayed, but it's not"