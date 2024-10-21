import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenario:
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        logged_in = LoggedInSuccessfullyPage(driver)

        # Open page
        # login_page.open()

        # Type username, password , submit button
        login_page.execute_login("student", "Password123")

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert logged_in.expected_url == login_page.current_url , "Actual URL is not the same as the expected URL"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in.header == "Logged In Successfully", "Header is not expected"
        assert logged_in.content == "Congratulations student. You successfully logged in!" , "Content is not expected"

        # Verify button Log out is displayed on the new page
        assert logged_in.is_logout_button_is_displayed, "Logout button should be visible"
