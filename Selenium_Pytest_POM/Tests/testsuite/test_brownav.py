import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_BrowserCommands:

    def test_browser_commands(self):

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Navigate to URL
        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(2)

        #Browser interactions
        title = driver.title
        print("Title:", title)

        url = driver.current_url
        print("Current URL:", url)

        time.sleep(2)

        #Navigational commands
        driver.back()
        time.sleep(2)

        driver.forward()
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

        driver.quit()