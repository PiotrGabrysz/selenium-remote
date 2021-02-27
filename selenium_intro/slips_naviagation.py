from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("http://automationpractice.com")
driver.implicitly_wait(5)

LOGIN_BUTTON_SELECTOR = "login"
EMAIL_FIELD_SELECTOR = "email"

driver.find_element_by_class_name(LOGIN_BUTTON_SELECTOR).click()
driver.find_element_by_id(EMAIL_FIELD_SELECTOR).send_keys("seleniumremote@gmail.com")
driver.find_element_by_id("passwd").send_keys("test123")
driver.find_element_by_id("SubmitLogin").click()
driver.find_element_by_xpath("//a[@title='Addresses']").click()

//div[@class='addresses']//div
//div[@class='credit-slips']//div

driver.quit()