"""
cart_page.py

Page Object Model for Cart / Bag functionality
of https://bstackdemo.com

This module handles:

- Opening Bag
- Fetching cart products
- Validating product prices
- Validating subtotal
- Checkout action
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        """
        Constructor initializes driver and explicit wait
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS -----------

    CART_ICON = (By.CLASS_NAME, "bag")

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".shelf-item__details .title")

    CART_PRODUCTS = (By.CSS_SELECTOR, ".shelf-item__details .title")

    CART_PRICES = (By.CSS_SELECTOR, ".shelf-item__price")

    SUBTOTAL = (By.CLASS_NAME, "sub-price")

    CHECKOUT_BTN = (By.XPATH, "//div[text()='Checkout']")

    # ----------- METHODS -----------

    def open_cart(self):
        """
        Click on cart/bag icon to open cart sidebar
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def get_cart_products(self):
        """
        Returns list of product names present in cart
        """
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.CART_PRODUCTS)
        )

        return [e.text for e in elements]

    def get_cart_prices(self):
        """
        Returns list of product prices
        """
        prices = self.wait.until(
            EC.presence_of_all_elements_located(self.CART_PRICES)
        )

        return [p.text for p in prices]

    def get_subtotal(self):
        """
        Fetch subtotal value displayed in cart
        """
        return self.wait.until(
            EC.visibility_of_element_located(self.SUBTOTAL)
        ).text

    def click_checkout(self):
        """
        Click checkout button
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BTN)
        ).click()