import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def test_radio():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(4)
    simple_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    simple_alert.click()
    #simple alert with okay button onlly
    alt=driver.switch_to.alert
    alt.accept()
    time.sleep(4)

    #confirmation Alert
    conf_alert = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    conf_alert.click()
    # simple alert with okay button onlly
    alt = driver.switch_to.alert
    alt.dismiss()
    time.sleep(4)

    #prompt Alert
    prompt_alert = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    prompt_alert.click()
    # simple alert with okay button onlly
    alt = driver.switch_to.alert
    alttext=alt.text
    print(alttext)
    alt.send_keys("HELLO JS")

    alt.accept()
    time.sleep(4)



    driver.quit()
