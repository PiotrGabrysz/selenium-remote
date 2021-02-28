from selenium.webdriver.common.by import By

from selenium_pop.pages.base import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON_SELECTOR = (By.CLASS_NAME, "login")
    EMAIL_FIELD_SELECTOR = (By.ID, "email")
    PASSWORD_FIELD_SELECTOR = (By.ID, "passwd")
    SUBMIT_LOGIN_BUTTON_SELECTOR = (By.ID, "SubmitLogin")
    HEADER_USER_INFO_SELECTOR = (By.CLASS_NAME, "header_user_info")

    def navigate_to_login_form(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def login_with_credentials(self, email, password):
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)
        self.driver.find_element(*self.SUBMIT_LOGIN_BUTTON_SELECTOR).click()
        self.check_if_element_visible(self.HEADER_USER_INFO_SELECTOR)
