import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_PracticePage:

    def test_full_scenario(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        wait = WebDriverWait(driver, 10)

        # ==============================
        # Step 1: Suggestion Class Example
        # ==============================

        suggestion_box = wait.until(
            EC.element_to_be_clickable((By.ID, "autocomplete"))
        )

        suggestion_box.click()
        suggestion_box.send_keys("india")

        time.sleep(2)

        india_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='India']"))
        )
        india_option.click()

        time.sleep(2)


        # Step 2: Switch Window Example


        parent_window = driver.current_window_handle

        open_window_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "openwindow"))
        )
        open_window_btn.click()

        time.sleep(3)

        all_windows = driver.window_handles

        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                break

        print("Child Window Title:", driver.title)
        time.sleep(3)

        # Close child window
        driver.close()

        # Switch back to parent
        driver.switch_to.window(parent_window)

        print("Back to Parent Title:", driver.title)
        time.sleep(3)

        # Switch Tab Example


        parent_tab = driver.current_window_handle

        open_tab_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "opentab"))
        )
        open_tab_btn.click()

        time.sleep(3)

        all_tabs = driver.window_handles

        for tab in all_tabs:
            if tab != parent_tab:
                driver.switch_to.window(tab)
                break

        print("Child Tab Title:", driver.title)
        time.sleep(3)

        # Close child tab
        driver.close()

        # Switch back to parent tab
        driver.switch_to.window(parent_tab)

        print("Back to Parent Tab Title:", driver.title)
        time.sleep(3)
        # Locate  the web  table
        webtable = driver.find_element(By.XPATH, "//legend[normalize-space()='Element Displayed Example']")

        # Scroll to Webtable using JavaScriptExecutor
        driver.execute_script("arguments[0].scrollIntoView(true);", webtable)

        # Fetch specific cell data table 1

        celldata = driver.find_element(By.XPATH, "//table[@id='product']/tbody/tr[9]/td[4]")
        print("Cell Data:", celldata.text)

        assert "33" in celldata.text

        time.sleep(2)

        # Fetch specific cell data table 2

        celldata = driver.find_element(By.XPATH, "//table[@name='courses']/tbody/tr[10]/td[2]")
        print("Cell Data:", celldata.text)

        assert "Advanced Selenium Framework Pageobject, TestNG, Maven, Jenkins,C" in celldata.text

        time.sleep(2)

        # Step 4: iFrame Example


        # Scroll to iframe section
        iframe_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//legend[text()='iFrame Example']"))
        )

        driver.execute_script("arguments[0].scrollIntoView();", iframe_element)
        time.sleep(2)

        # Switch to iframe
        driver.switch_to.frame(0)  # Only one iframe on page

        time.sleep(2)

        # Get all text inside iframe
        iframe_text = driver.find_element(By.TAG_NAME, "body").text
        print("iFrame Text")
        print(iframe_text)

        time.sleep(3)

        # Switch back to main page
        driver.switch_to.default_content()







        driver.quit()