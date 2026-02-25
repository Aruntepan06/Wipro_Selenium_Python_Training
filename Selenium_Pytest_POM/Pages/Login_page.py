# Login page
# 1. verify login with valid credentials
# 2. verify login with invalid credentials
# 3. Verify password masking
# 4
# ...

from selenium.webdriver.common.by import By

import time
class LoginPage:

    # locators
    username_input = (By.XPATH, "//input[@placeholder='Username']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH,"//button[normalize-space()='Login']")
    # dashboard_text=(By.XPATH,"//div[@class='app_logo']")
    err_msg = (By.XPATH,"//div[@class='oxd-alert-content oxd-alert-content--error']")

    def __init__(self, driver):
        self.driver = driver

    def  enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self,username,password):
        self.enter_username(username)
        time.sleep(3)
        self.enter_password(password)
        time.sleep(2)
        self.click_login()
        time.sleep(3)

    def get_error_message(self):
        return self.driver.find_element(*self.err_msg).text