from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class USER_INFO:

    # locators
    firstname_input= (By.XPATH,"//input[@id='first-name']")
    lastname_input= (By.XPATH,"//input[@id='last-name']")
    postal_code_input= (By.XPATH,"//input[@id='postal-code']")
    continuebtn=(By.XPATH, "//input[@id='continue']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def firstname(self,firstname):
        self.driver.find_element(*self.firstname_input).send_keys(firstname)
    def lastname(self,lastname):
        self.driver.find_element(*self.lastname_input).send_keys(lastname)
    def postal_code(self,postal_code):
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def form(self,firstname,lastname,postal_code):
        self.firstname(firstname)
        time.sleep(3)
        self.lastname(lastname)
        time.sleep(3)
        self.postal_code(postal_code)
        time.sleep(3)
    def conbtn(self):
        self.driver.find_element(*self.continuebtn).click()
        time.sleep(3)




