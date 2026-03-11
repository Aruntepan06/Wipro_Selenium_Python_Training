"""
product_page.py

Page Object Model for the Product page of BrowserStack Demo store.

Responsibilities:
- Perform product search
- Click search button
- Add searched product to cart

This page class abstracts all locators and actions related to products.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        """
        Constructor for ProductPage

        Parameters
        ----------
        driver : WebDriver
            Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------------------------------------------------
    # Locators
    # ---------------------------------------------------

    # Search input box
    SEARCH_BOX = (By.XPATH, "//input[@placeholder='Search']")

    # Search button
    SEARCH_BUTTON = (By.XPATH, "//button[contains(.,'Search')]")

    # ---------------------------------------------------
    # Page Actions
    # ---------------------------------------------------

    def search_product(self, product_name):
        """
        Enter product name in the search box

        Parameters
        ----------
        product_name : str
            Name of the product to search
        """

        search = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )

        search.clear()
        search.send_keys(product_name)

    def click_search(self):
        """
        Click the search button to perform product search
        """

        search_btn = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        search_btn.click()

    def add_product_to_cart(self, product_name):
        """
        Click 'Add to cart' button for the searched product

        The locator dynamically finds the product card
        and then clicks the Add to cart button.

        Parameters
        ----------
        product_name : str
        """

        add_to_cart = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//p[text()='{product_name}']/following::div[text()='Add to cart'][1]"
                )
            )
        )

        add_to_cart.click()