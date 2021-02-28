import unittest

from selenium_pop.config import *
from selenium_pop.pages.search import SearchPage
from selenium_pop.utils import get_driver


class SearchTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(BROWSER)
        self.driver.get(URL)

        self.search_page = SearchPage(self.driver)

    def test_non_existing_product(self):
        self.search_page.search_item("test")
        self.search_page.check_if_alert_appears()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
