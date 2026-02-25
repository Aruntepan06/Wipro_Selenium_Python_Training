import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_GreenKart:
    def test_complete_order_flow(self):
        driver = None
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

            time.sleep(3)

            # Add first 4 products
            products = driver.find_elements(By.CSS_SELECTOR, "div.product")

            for i in range(4):
                products[i].find_element(By.TAG_NAME, "button").click()
                time.sleep(1)

            # Click cart
            driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
            time.sleep(2)

            # Proceed to checkout
            driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
            time.sleep(3)

            # Validate total price
            total_amount = driver.find_element(By.CLASS_NAME, "totAmt").text
            assert total_amount == "260"

            # Click Place Order
            driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
            time.sleep(2)

            # Select India from dropdown
            dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
            dropdown.select_by_visible_text("India")
            time.sleep(2)

            # Click Agree checkbox
            driver.find_element(By.CLASS_NAME, "chkAgree").click()
            time.sleep(1)

            # Click Proceed
            driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
            time.sleep(3)

        except Exception as e:
            print("Test Failed:", e)
            raise

        finally:
            if driver:
                driver.quit()