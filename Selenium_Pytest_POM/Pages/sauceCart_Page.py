from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SauceCart:

    # locators

    checkoutbtn=(By.XPATH, "//button[@id='checkout']")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        self.driver.find_element(*self.checkoutbtn).click()


