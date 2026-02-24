import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_radio():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    time.sleep(4)
    radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
    radio_btn.click()
    time.sleep(2)
    check2_btn = driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']")
    check2_btn.click()
    time.sleep(2)
    check3_btn = driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']")
    check3_btn.click()
    driver.quit()
