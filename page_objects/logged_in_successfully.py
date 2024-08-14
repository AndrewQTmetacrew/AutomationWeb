from selenium.webdriver.common.by import By
from selenium import webdriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __title_locator = (By.TAG_NAME, "h1")
    __content_locator = (By.XPATH, "//div[@class= 'post-content']/p[@class= 'has-text-align-center']")
    __logout_btn_locator = (By.PARTIAL_LINK_TEXT, "Log")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return super().get_text(self.__title_locator)

    @property
    def content(self) -> str:
        return super().get_text(self.__content_locator)

    @property
    def is_logout_button_is_displayed(self) -> bool:
        return super().is_displayed(self.__logout_btn_locator)
