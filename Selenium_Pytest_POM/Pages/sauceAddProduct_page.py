from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SauceAddProductPage:

    # locators
    addprod=(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    # make title strict for cart page
    cart_title = (By.XPATH, "//span[@class='title']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_prod(self):
        self.driver.find_element(*self.addprod).click()
        time.sleep(1)

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        # wait until cart title shows "Your Cart"
        self.wait.until(EC.visibility_of_element_located(self.cart_title))

    def get_cart_title(self):
        return self.driver.find_element(*self.cart_title).text



