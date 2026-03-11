"""
Login Page Object

Contains all locators and actions related to login functionality
for https://bstackdemo.com
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------------- LOCATORS ---------------- #

    SIGN_IN = (By.ID, "signin")

    USERNAME_DROPDOWN = (By.ID, "username")
    PASSWORD_DROPDOWN = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login-btn")

    PRODUCT_LIST = (By.XPATH, "//div[contains(@class,'shelf-item')]")

    # Username options
    DEMO_USER = (By.XPATH, "//div[text()='demouser']")
    LOCKED_USER = (By.XPATH, "//div[text()='locked_user']")
    IMAGE_USER = (By.XPATH, "//div[text()='image_not_loading_user']")
    EXISTING_USER = (By.XPATH, "//div[text()='existing_orders_user']")
    FAV_USER = (By.XPATH, "//div[text()='fav_user']")

    PASSWORD_OPTION = (By.XPATH, "//div[text()='testingisfun99']")

    # ---------------- ACTION METHODS ---------------- #

    def open_login_popup(self):
        """Click sign in button"""
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN)).click()

    def select_username(self, user_locator):
        """Select username from dropdown"""
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(user_locator)).click()

    def select_password(self):
        """Select password from dropdown"""
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_OPTION)).click()

    def click_login(self):
        """Click login button"""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, user_locator):
        """Complete login flow"""
        self.open_login_popup()
        self.select_username(user_locator)
        self.select_password()
        self.click_login()

    def is_login_successful(self):
        """Verify products page loads"""
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_LIST)
        )