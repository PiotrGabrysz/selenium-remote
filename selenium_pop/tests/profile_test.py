import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from hamcrest import *

from selenium_pop.config import *
from selenium_pop.pages.login import LoginPage
from selenium_pop.pages.profile import ProfilePage

class ProfileTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(TIMEOUT)
        self.driver.get(URL)

        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

        self.login_page.navigate_to_login_form()
        self.login_page.login_with_credentials(VALID_EMAIL, VALID_PASSWORD)

    def test_my_addresses(self):
        self.profile_page.navigate_to_addresses()
        addresses = self.profile_page.get_all_address()
        assert_that(len(addresses), greater_than_or_equal_to(1))

    def test_my_credit_slips(self):
        self.profile_page.navigate_to_credit_slips()
        credit_slips = self.profile_page.get_all_credit_slips()
        assert_that(len(credit_slips), greater_than_or_equal_to(1))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
