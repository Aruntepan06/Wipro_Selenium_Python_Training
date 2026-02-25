import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



DOWNLOAD_DIR = "/Users/arunkumartepan/Downloads/"


class Test_download:

    def test_dw(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": DOWNLOAD_DIR,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        alert = driver.find_element(By.XPATH, "//a[normalize-space()='alert.jpeg']")
        alert.click()

        time.sleep(3)  # wait for download

        # Verify file downloaded
        file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(file_path)

        time.sleep(2)
        driver.quit()