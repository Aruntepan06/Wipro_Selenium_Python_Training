import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager


class Test_waits:

    def test_waits(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()

        # implicit wait
        driver.implicitly_wait(2)

        # explicit wait
        radio_btn = driver.find_element(By.XPATH, "((//input[@value='radio2'])[1])")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _: radio_btn.is_displayed())

        # fluent wait
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout=2, poll_frequency=0.2, ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.send_keys("Displayed") or True)

        driver.quit()