from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("http://automationpractice.com")


driver.find_element_by_class_name("shop-phone")

# elements = driver.find_elements_by_class_name("product-container-test")
# assert elements, "Elements not found"


driver.quit()
