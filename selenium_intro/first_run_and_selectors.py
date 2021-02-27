from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("http://automationpractice.com")


driver.find_element_by_class_name("shop-phone")

# simple selectors
driver.find_element_by_id("header_logo")
driver.find_element_by_partial_link_text("Cart")
driver.find_element_by_id("newsletter-input")
driver.find_element_by_class_name("twitter")
driver.find_element_by_class_name("homefeatured")
driver.find_element_by_id("contact-link")

# css selectors
driver.find_element_by_css_selector("#header_logo")
driver.find_element_by_css_selector(".shopping_cart > a")
driver.find_element_by_css_selector("#newsletter-input")
driver.find_element_by_css_selector(".twitter")
driver.find_element_by_css_selector('[href="#homefeatured"]')  # same as .homefeatured
driver.find_element_by_css_selector("#contact-link")

# path selectors


# elements = driver.find_elements_by_class_name("product-container-test")
# assert elements, "Elements not found"


driver.quit()

