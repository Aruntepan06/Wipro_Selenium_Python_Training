from selenium.webdriver.common.by import By

import time
class LoginPage:

    # locators
    username_input = (By.XPATH, "//input[@id='user-name']")
    password_input = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH,"//input[@id='login-button']")
    # dashboard_text=(By.XPATH,"//div[@class='app_logo']")
    err_msg = (By.XPATH,"//h3[contains(text(),'Epic sadface: Username and password do not match a')]")

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