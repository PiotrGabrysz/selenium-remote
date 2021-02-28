from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_pop.config import TIMEOUT


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def check_if_element_visible(self, selector):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(selector))
