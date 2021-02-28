from selenium.webdriver.common.by import By

from selenium_pop.pages.base import BasePage


class SearchPage(BasePage):

    ALERT_WARNING_SELECTOR = (By.XPATH, "//*[@class='alert alert-warning']")
    SEARCH_FILED_SELECTOR = (By.ID, "search_query_top")
    SUBMIT_SEARCH_SELECTOR = (By.NAME, "submit_search")

    def search_item(self, name):
        self.driver.find_element(*self.SEARCH_FILED_SELECTOR).send_keys(name)
        self.driver.find_element(*self.SUBMIT_SEARCH_SELECTOR).click()

    def check_if_alert_appears(self):
        self.check_if_element_visible(self.ALERT_WARNING_SELECTOR)
