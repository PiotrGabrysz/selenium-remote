from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# DRIVER SET-UP
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("http://automationpractice.com")
driver.implicitly_wait(5)


# SELECTORS HERE
LOGIN_BUTTON_SELECTOR = (By.CLASS_NAME, "login")
EMAIL_FIELD_SELECTOR = (By.ID, "email")
PASSWORD_FIELD_SELECTOR = (By.ID, "passwd")
SUBMIT_LOGIN_BUTTON_SELECOTR = (By.ID, "SubmitLogin")
ADDRESSES_BUTTON_SELECTOR = (By.XPATH, "//a[@title='Addresses']")
CREDIT_SLIPS_BUTTON_SELECTOR = (By.XPATH, "//a[@title='Credit slips']")
MY_ADDRESSES_SELECTOR = (By.XPATH, "//div[@class='addresses']//div")
MY_CREDIT_SLIPS_SELECTOR = (By.XPATH, "//div[@class='credit-slips']//div")


# LOGIC HERE
driver.find_element(*LOGIN_BUTTON_SELECTOR).click()
driver.find_element(*EMAIL_FIELD_SELECTOR).send_keys("seleniumremote@gmail.com")
driver.find_element(*PASSWORD_FIELD_SELECTOR).send_keys("test123")
driver.find_element(*SUBMIT_LOGIN_BUTTON_SELECOTR).click()
driver.find_element(*ADDRESSES_BUTTON_SELECTOR).click()

# addresses check
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(MY_ADDRESSES_SELECTOR))

driver.back()
driver.find_element(*CREDIT_SLIPS_BUTTON_SELECTOR).click()

# credit slips check
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(MY_CREDIT_SLIPS_SELECTOR))

driver.quit()
