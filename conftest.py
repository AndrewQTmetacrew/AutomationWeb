import os
import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup_env():
    env = int(os.getenv("ENV"))
    env_urls = {
        1: "https://practicetestautomation.com/practice-test-login/",
        2: "",
        3: ""
    }
    url = env_urls.get(env)
    if not url:
        pytest.fail("Environment invalid")
    yield url


# @pytest.fixture(params=["chrome", "firefox", "edge"], scope="session")
@pytest.fixture(scope="session")
def driver(request, setup_env):
    browser = request.config.getoption('--browser')
    # browser = request.param
    # Open browser
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        pytest.fail("Unsupported browser")
    # Go to webpage
    driver.get(setup_env)
    yield driver
    time.sleep(1)
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        help="browser to use for testing (chrome, firefox, edge)"
    )
