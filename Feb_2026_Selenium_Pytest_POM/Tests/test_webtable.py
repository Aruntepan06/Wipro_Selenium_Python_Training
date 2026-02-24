import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_WebTable:

    def test_table(self):

        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Open URL
        driver.get("https://the-internet.herokuapp.com/tables")
        time.sleep(3)


        # Number of rows

        rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
        print("Number of rows:", len(rows))

        for i in rows:
            print(i.text)

        time.sleep(2)


        # Number of columns (from first row)

        cols = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")
        print("Number of columns:", len(cols))

        for i in cols:
            print(i.text)

        time.sleep(2)


        # Fetch specific cell data (3rd row, 4th column)

        celldata = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]")
        print("Cell Data:", celldata.text)

        assert "$100.00" in celldata.text

        time.sleep(2)
        driver.quit()