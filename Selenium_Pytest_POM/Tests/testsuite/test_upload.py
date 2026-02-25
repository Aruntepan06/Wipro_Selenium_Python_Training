import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Upload:

    def test_up(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        # Locate file upload input
        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")

        # Provide full file path (change to your actual file path on Mac)
        browse.send_keys("/Users/arunkumartepan/Downloads/sampleFile.png")
        time.sleep(2)

        # Click upload button
        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload.click()
        time.sleep(2)

        # Verify upload success
        fileupload = driver.find_element(By.XPATH, "//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.quit()