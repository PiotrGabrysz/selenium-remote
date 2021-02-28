from selenium.webdriver.common.by import By

from selenium_pop.pages.base import BasePage


class SummaryPage(BasePage):

    TOTAL_SHIPPING_SELECTOR = (By.ID, "total_shipping")
    TOTAL_PRICE_SELECTOR = (By.ID, "total_price")

    def get_total_price(self):
        price_element = self.driver.find_element(*self.TOTAL_PRICE_SELECTOR).text
        total_price = float(price_element[1:])
        return total_price

    def get_shipping_price(self):
        shipping_element = self.driver.find_element(*self.TOTAL_SHIPPING_SELECTOR).text
        shipping_price = float(shipping_element[1:])
        return shipping_price
