from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium_pop.config import TIMEOUT


def get_driver(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise NameError(f"{browser} not found")
    driver.implicitly_wait(TIMEOUT)
    return driver
