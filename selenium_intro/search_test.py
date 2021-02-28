import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class SearchTest(unittest.TestCase):

    ALERT_WARNING_SELECTOR = (By.XPATH, "//*[@class='alert alert-warning']")
    SEARCH_FILED_SELECTOR = (By.ID, "search_query_top")
    SUBMIT_SEARCH_SELECTOR = (By.NAME, "submit_search")

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        # options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("http://automationpractice.com")

    def test_non_existing_product(self):
        self.driver.find_element(*self.SEARCH_FILED_SELECTOR).send_keys("test")
        self.driver.find_element(*self.SUBMIT_SEARCH_SELECTOR).click()

        # driver.find_element_by_xpath("//*[@class='alert alert-warning']") - not recommended due to loading delay
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ALERT_WARNING_SELECTOR))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
