import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):

    LOGIN_BUTTON_SELECTOR = (By.CLASS_NAME, "login")
    EMAIL_FIELD_SELECTOR = (By.ID, "email")
    PASSWORD_FIELD_SELECTOR = (By.ID, "passwd")
    SUBMIT_LOGIN_BUTTON_SELECOTR = (By.ID, "SubmitLogin")
    ADDRESSES_BUTTON_SELECTOR = (By.XPATH, "//a[@title='Addresses']")
    CREDIT_SLIPS_BUTTON_SELECTOR = (By.XPATH, "//a[@title='Credit slips']")
    MY_ADDRESSES_SELECTOR = (By.XPATH, "//div[@class='addresses']//div")
    MY_CREDIT_SLIPS_SELECTOR = (By.XPATH, "//div[@class='credit-slips']//div")

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("http://automationpractice.com")


        # Login action
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys("seleniumremote@gmail.com")
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys("test123")
        self.driver.find_element(*self.SUBMIT_LOGIN_BUTTON_SELECOTR).click()

    def test_my_addresses(self):
        self.driver.find_element(*self.ADDRESSES_BUTTON_SELECTOR).click()

        # addresses check
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MY_ADDRESSES_SELECTOR))

    def test_credit_slips(self):
        self.driver.find_element(*self.CREDIT_SLIPS_BUTTON_SELECTOR).click()

        # credit slips check
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MY_CREDIT_SLIPS_SELECTOR))

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
