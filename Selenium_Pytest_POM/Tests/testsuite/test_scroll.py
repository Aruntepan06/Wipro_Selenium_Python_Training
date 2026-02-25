import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Scroll:

    def test_scroll_to_instagram(self):

        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Open website
        driver.get("https://www.amazon.in/")
        time.sleep(3)
        # Assert title
        assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" in driver.title

        # Locate Instagram link
        instagram = driver.find_element(By.XPATH, "//a[normalize-space()='Instagram']")

        # Scroll to Instagram using JavaScriptExecutor
        driver.execute_script("arguments[0].scrollIntoView(true);", instagram)

        time.sleep(3)
        # Vertical up scroll (X coordinate = 0, scroll up by 1000 pixels)
        driver.execute_script("window.scrollBy(0, -1000)")
        time.sleep(2)

        # Vertical down scroll (X coordinate = 0, scroll down by 5000 pixels)
        driver.execute_script("window.scrollBy(0, 5000)")

        # Close browser
        driver.quit()
