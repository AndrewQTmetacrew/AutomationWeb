import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.exceptions_page import ExceptionPage


class TestException:
    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_no_such_element_exception(self, driver):
        exception_action1 = ExceptionPage(driver)
        # Open page
        exception_action1.open()

        # Click Add button
        exception_action1.add_second_row()

        # Verify row2 input is displayed
        assert exception_action1.is_row2_displayed, "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self):
        #Open page
        driver = webdriver.Edge()
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instructions_locator = driver.find_element(By.XPATH, "//p[@id='instructions']")
        assert instructions_locator.is_displayed(), "Instructions is not displayed"
        # Push add button
        add_btn_locator = driver.find_element(By.XPATH, "//div[@id= 'row1']/button[@id='add_btn']")
        # add_btn_locator.click()
        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.invisibility_of_element_located((By.XPATH, "//p[@id='instructions']"))), \
            "Instructtion is no longer visible"

    @pytest.mark.exceptions
    def test_timeout_exception(self):
        #Open page
        driver = webdriver.Edge()
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_btn_locator = driver.find_element(By.XPATH, "//div[@id= 'row1']/button[@id='add_btn']")
        add_btn_locator.click()
        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 30)
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input"))), \
            "Second input field is not displayed"
        # Verify second input field is displayed
