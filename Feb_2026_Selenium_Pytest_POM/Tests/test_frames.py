import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Frame:

    def test_frame(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Switch to iframe
        frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(frame)

        # Click on datepicker input
        datepicker = driver.find_element(By.ID, "datepicker")
        datepicker.click()

        time.sleep(3)

        # Switch back to main page
        driver.switch_to.default_content()

        driver.quit()