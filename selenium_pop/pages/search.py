from selenium.webdriver.common.by import By

from selenium_pop.pages.base import BasePage


class SearchPage(BasePage):

    ALERT_WARNING_SELECTOR = (By.XPATH, "//*[@class='alert alert-warning']")
    SEARCH_FILED_SELECTOR = (By.ID, "search_query_top")
    SUBMIT_SEARCH_SELECTOR = (By.NAME, "submit_search")
    PRODUCT_CONTAINER_SELECTOR = (By.CLASS_NAME, "product-container")
    ADD_TO_CART_BUTTON_SELECTOR = (By.CSS_SELECTOR, ".ajax_add_to_cart_button")
    PROCEED_TO_CHECKOUT_SELECTOR = (By.XPATH, "//*[@title='Proceed to checkout']")

    def search_item(self, name):
        self.driver.find_element(*self.SEARCH_FILED_SELECTOR).send_keys(name)
        self.driver.find_element(*self.SUBMIT_SEARCH_SELECTOR).click()

    def check_if_alert_appears(self):
        self.check_if_element_visible(self.ALERT_WARNING_SELECTOR)

    def add_to_cart(self):
        product_element = self.driver.find_element(*self.PRODUCT_CONTAINER_SELECTOR)
        self.hover_mouse_over(product_element)
        self.driver.find_element(*self.ADD_TO_CART_BUTTON_SELECTOR).click()
        self.check_if_element_visible(self.PROCEED_TO_CHECKOUT_SELECTOR)

    def proceed_to_checkout(self):
        self.driver.find_element(*self.PROCEED_TO_CHECKOUT_SELECTOR).click()