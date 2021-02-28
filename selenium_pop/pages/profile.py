from selenium.webdriver.common.by import By

from selenium_pop.pages.base import BasePage


class ProfilePage(BasePage):

    ADDRESSES_BUTTON_SELECTOR = (By.XPATH, "//a[@title='Addresses']")
    CREDIT_SLIPS_BUTTON_SELECTOR = (By.XPATH, "//a[@title='Credit slips']")
    MY_ADDRESSES_SELECTOR = (By.XPATH, "//div[@class='addresses']//div")
    MY_CREDIT_SLIPS_SELECTOR = (By.XPATH, "//div[@class='credit-slips']//div")

    def navigate_to_addresses(self):
        self.driver.find_element(*self.ADDRESSES_BUTTON_SELECTOR).click()

    def get_all_address(self):
        addresses = self.driver.find_elements(*self.MY_ADDRESSES_SELECTOR)
        return addresses

    def navigate_to_credit_slips(self):
        self.driver.find_element(*self.CREDIT_SLIPS_BUTTON_SELECTOR).click()

    def get_all_credit_slips(self):
        credit_slips = self.driver.find_elements(*self.MY_CREDIT_SLIPS_SELECTOR)
        return credit_slips
