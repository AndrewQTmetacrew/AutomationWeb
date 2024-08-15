from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: webdriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str,str], text: str, time: int = 10):
        self._wait_until_element_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple[str,str], time: int = 10):
        self._wait_until_element_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_visible(self, locator: tuple[str,str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def open_url(self, url: str):
        self._driver.get(url)

    def get_text(self, locator: tuple[str,str], time: int = 10) -> str:
        self._wait_until_element_visible(locator, time)
        return self._find(locator).text