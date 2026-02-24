import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Links:

    def test_dw(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        # Find all links
        links = driver.find_elements(By.TAG_NAME, "a")
        count = len(links)
        print(count)

        # Print all link texts
        for link in links:
            print(link.text)

        time.sleep(2)
        driver.quit()