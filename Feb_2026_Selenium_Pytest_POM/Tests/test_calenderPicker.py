import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_DatePicker:

    def test_select_24_feb_2026(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://rsuitejs.com/components/date-picker/")
        time.sleep(3)

        # Scroll to Basic section
        basic_heading = driver.find_element(By.ID, "basic")
        driver.execute_script("arguments[0].scrollIntoView();", basic_heading)
        time.sleep(2)

        # Click date input
        date_input = driver.find_element(By.XPATH, "//input[@id='rs-:r2b:']")
        date_input.click()
        time.sleep(2)

        # Click Feb 24, 2026
        date_to_click = driver.find_element(
            By.XPATH,
            "//div[@role='gridcell' and @aria-label='Feb 24, 2026']"
        )
        date_to_click.click()
        time.sleep(3)
        # Click OK button
        ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        ok_button.click()
        time.sleep(2)

        driver.quit()