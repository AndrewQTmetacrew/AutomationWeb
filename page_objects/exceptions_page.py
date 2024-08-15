from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_btn_locator = (By.ID, "add_btn")
    __row1_input_locator = (By.XPATH, "//div[@id='row1']/input")
    __row2_input_locator = (By.XPATH, "//div[@id='row2']/input")
    __row2_save_btn_locator = (By.XPATH, "//div[@id = 'row2']/button[@name= 'Save']")
    __confirmation_message = (By.XPATH, "//div[@id = 'confirmation']")
    __row1_edit_button = (By.XPATH, "//div[@id='row1']/button[@id= 'edit_btn']")
    __row1_save_btn_locator = (By.XPATH, "//div[@id='row1']/button[@name= 'Save']")
    __instructions_locator = (By.XPATH, "//p[@id = 'instructions']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_btn_locator)
        super()._wait_until_element_visible(self.__row2_input_locator)

    @property
    def is_row2_displayed(self) -> bool:
        return super().is_displayed(self.__row2_input_locator)

    def add_row2_food(self, text: str):
        super()._type(self.__row2_input_locator, text)
        super()._click(self.__row2_save_btn_locator)
        super()._wait_until_element_visible(self.__confirmation_message, 3)

    @property
    def get_confirmation_message(self)-> str:
        return super().get_text(self.__confirmation_message, 3)

    def modify_row1_input(self, text: str):
        super()._click(self.__row1_edit_button)
        super()._wait_until_element_clickable(self.__row1_input_locator)
        super()._clear(self.__row1_input_locator)
        super()._type(self.__row1_input_locator, text)
        super()._click(self.__row1_save_btn_locator)
        super()._wait_until_element_visible(self.__confirmation_message)

    @property
    def is_instructions_displayed(self) -> bool:
        return super().is_displayed(self.__instructions_locator)