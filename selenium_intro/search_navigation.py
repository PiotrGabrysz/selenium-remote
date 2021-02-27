from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)

driver.get("http://automationpractice.com")

driver.find_element_by_id("search_query_top").send_keys("test")
driver.find_element_by_name("submit_search").click()

# driver.find_element_by_xpath("//*[@class='alert alert-warning']") - not recommended due to loading delay
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@class='alert alert-warning']")))

driver.quit()