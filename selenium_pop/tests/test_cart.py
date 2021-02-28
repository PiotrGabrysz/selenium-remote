import unittest
from hamcrest import *

from selenium_pop.utils import get_driver
from selenium_pop.config import *
from selenium_pop.pages.search import SearchPage
from selenium_pop.pages.summary import SummaryPage


class CartTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(BROWSER)
        self.driver.get(URL)

        self.search_page = SearchPage(self.driver)

    def test_single_dress_item(self):
        self.search_page.search_item("Printed Summer")
        self.search_page.add_to_cart()


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
