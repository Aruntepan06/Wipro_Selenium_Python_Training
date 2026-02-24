import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Keyboard:

    def test_Keyboard(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(3)

        # Email
        email = driver.find_element(By.XPATH, "//input[@name='email']")
        email.click()
        email.send_keys("aruntepan19@gmail.com")
        time.sleep(1)

        # CMD + A (Select All)
        email.send_keys(Keys.COMMAND + "a")
        time.sleep(1)

        # CMD + C (Copy)
        email.send_keys(Keys.COMMAND + "c")
        time.sleep(1)

        # Password (use stable locator)
        password = driver.find_element(By.XPATH, "//input[@name='pass']")
        password.click()
        time.sleep(1)

        # CMD + V (Paste)
        password.send_keys(Keys.COMMAND + "v")
        time.sleep(2)

        eye_button = driver.find_element(
            By.XPATH,
            "//div[@aria-label='Show password']//*[name()='svg']"
        )
        eye_button.click()

        time.sleep(5)
        driver.quit()