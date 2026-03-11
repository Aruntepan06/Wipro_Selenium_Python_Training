"""
order_confirmation_page.py

Handles actions on the Order Confirmation page.

Features:
✔ Download order receipt
✔ Verify receipt download
✔ Continue shopping
"""

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderConfirmationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # LOCATORS

    DOWNLOAD_RECEIPT = (By.ID, "downloadpdf")

    CONTINUE_SHOPPING = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")

    # METHODS

    def click_download_receipt(self):
        """
        Click download receipt link
        """
        self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_RECEIPT)
        ).click()

    def is_receipt_downloaded(self, file_path):
        """
        Check if receipt file exists in Downloads
        """
        return os.path.exists(file_path)

    def click_continue_shopping(self):
        """
        Click continue shopping button
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        ).click()