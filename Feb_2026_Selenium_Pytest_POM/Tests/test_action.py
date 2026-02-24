import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Action:

    def test_action(self):

        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Create ActionChains object
        actions = ActionChains(driver)

        # Open website
        driver.get("https://www.amazon.in/")
        time.sleep(3)

        # Assert title
        assert "Amazon.in" in driver.title

        # Locate Bestsellers
        bestsellers = driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")

        # Double click using ActionChains
        actions.double_click(bestsellers).perform()
        time.sleep(3)

        driver.back()
        time.sleep(3)

        # Locate Mobiles
        mobiles = driver.find_element(By.XPATH, "//a[normalize-space()='Mobiles']")

        # Right click using ActionChains
        actions.context_click(mobiles).perform()
        driver.back()
        time.sleep(3)

        # move to element
        primes = driver.find_element(By.XPATH, "//span[normalize-space()='Prime']")
        actions.move_to_element(primes).perform()
        time.sleep(5)

        # click and hold
        fresh = driver.find_element(By.XPATH, "//a[normalize-space()='Fresh']")
        actions.click_and_hold(fresh).perform()
        time.sleep(3)
        driver.quit()