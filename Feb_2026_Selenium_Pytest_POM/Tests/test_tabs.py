import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_tabs_chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    time.sleep(2)

    clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
    clickhere.click()
    time.sleep(2)

    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
    assert text.text == "New Window"

    driver.close()
    driver.switch_to.window(windows[0])
    time.sleep(2)

    driver.quit()