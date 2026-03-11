"""
checkout_page.py

Handles Checkout Shipping Address Page

Functions:
- Fill shipping form
-Submit order
-Validate order summary
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators

    FIRSTNAME = (By.ID, "firstNameInput")
    LASTNAME = (By.ID, "lastNameInput")
    ADDRESS = (By.ID, "addressLine1Input")
    STATE = (By.ID, "provinceInput")
    POSTAL = (By.ID, "postCodeInput")
    SUBMIT = (By.ID, "checkout-shipping-continue")

    # Methods

    def enter_first_name(self, firstname):
        self.wait.until(EC.visibility_of_element_located(self.FIRSTNAME)).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.LASTNAME).send_keys(lastname)

    def enter_address(self, address):
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    def enter_state(self, state):
        self.driver.find_element(*self.STATE).send_keys(state)

    def enter_postal_code(self, postal):
        self.driver.find_element(*self.POSTAL).send_keys(postal)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()