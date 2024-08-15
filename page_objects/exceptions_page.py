from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_btn = (By.ID, "add_btn")
    __row1_locator = (By.XPATH, "//div[@id='row1']/input")
    __row2_locator = (By.XPATH, "//div[@id='row2']/input")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_btn)
        super()._wait_until_element_visible(self.__row2_locator)

    @property
    def is_row2_displayed(self) -> bool:
        return super().is_displayed(self.__row2_locator)