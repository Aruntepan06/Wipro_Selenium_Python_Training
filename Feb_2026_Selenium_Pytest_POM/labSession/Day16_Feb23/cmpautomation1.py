import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_login:
    def test_login(self):
        driver = None
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")

            time.sleep(2)

            # Login
            driver.find_element(By.NAME, "user-name").send_keys("standard_user")
            driver.find_element(By.NAME, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()

            time.sleep(3)

            # Add product to cart
            driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            time.sleep(2)

            # Open cart page
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            time.sleep(2)

            # Click Checkout
            driver.find_element(By.ID, "checkout").click()
            time.sleep(2)

            # Fill checkout form
            driver.find_element(By.ID, "first-name").send_keys("Arun")
            driver.find_element(By.ID, "last-name").send_keys("Test")
            driver.find_element(By.ID, "postal-code").send_keys("560001")
            time.sleep(2)

            # Continue to overview
            driver.find_element(By.ID, "continue").click()
            time.sleep(3)

            # Validate you are on Checkout: Overview page
            overview_title = driver.find_element(By.CSS_SELECTOR, "span.title").text
            assert overview_title == "Checkout: Overview"

            time.sleep(2)

            # Click Finish
            driver.find_element(By.ID, "finish").click()
            time.sleep(3)

            # Validate checkout is completed
            complete_title = driver.find_element(By.CSS_SELECTOR, "span.title").text
            assert complete_title == "Checkout: Complete!"

        except Exception as e:
            print("Test Failed due to:", e)
            raise

        finally:
            if driver:
                driver.quit()