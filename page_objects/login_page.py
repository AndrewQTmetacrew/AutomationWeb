from selenium.webdriver.common.by import By
from selenium import webdriver

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = 'https://practicetestautomation.com/practice-test-login/'
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.ID, "submit")
    __error_message_locator = (By.ID, "error")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    @property
    def error_message_text(self) -> str:
        return super().get_text(self.__error_message_locator,3)