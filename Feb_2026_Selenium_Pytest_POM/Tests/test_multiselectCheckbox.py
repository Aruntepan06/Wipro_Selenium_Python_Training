import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_MultiSelectCheckbox:

    def test_multiselect2(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        time.sleep(4)

        # enter username
        name = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        name.send_keys("Admin")

        # enter password
        password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password.send_keys("admin123")

        time.sleep(2)

        # click login button
        Login = driver.find_element(By.XPATH, "//button[@type='submit']")
        Login.click()

        time.sleep(5)

        # click PIM menu
        PIM = driver.find_element(By.XPATH, "//span[normalize-space()='PIM']")
        PIM.click()

        time.sleep(5)

        # scroll page
        driver.execute_script("window.scrollTo(0,500);")
        time.sleep(2)

        # correct checkbox locator (table row checkboxes)
        checkbox_list = driver.find_elements(
            By.XPATH,
            "//div[@class='oxd-table-body']//i[contains(@class,'oxd-checkbox-input-icon')]"
        )

        count = len(checkbox_list)
        print(count)

        # click all checkboxes
        for i in checkbox_list:
            time.sleep(1)
            i.click()

        driver.quit()