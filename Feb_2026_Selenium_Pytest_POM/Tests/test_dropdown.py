import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class Test_DropDp:

    # def test_radio(self):
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     driver.maximize_window()
    #
    #     driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    #
    #     time.sleep(4)
    #
    #     dropdown = driver.find_element(By.ID, "dropdown-class-example")
    #     # select class is used for drop downs
    #     sel = Select(dropdown)
    #
    #     # select by visible text or label
    #     sel.select_by_visible_text("Option1")
    #     time.sleep(2)
    #
    #     sel.select_by_value("option2")
    #     time.sleep(2)
    #
    #     sel.select_by_index(3)
    #     time.sleep(2)
    #
    #     driver.quit()

    def test_radio2(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(4)
        element = driver.find_element(By.ID, "option")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        dropdown = driver.find_element(By.NAME, "option")
        # select class is used for drop downs
        sel = Select(dropdown)

        # select by visible text or label
        sel.select_by_visible_text("Option 1")
        time.sleep(2)

        sel.select_by_value("option 2")
        time.sleep(2)

        sel.select_by_index(3)
        time.sleep(2)

        dropdown = driver.find_element(By.ID, "owc")
        # select class is used for drop downs
        sel = Select(dropdown)

        sel.select_by_visible_text("Option 1")
        time.sleep(2)

        sel.select_by_value("option 2")
        time.sleep(2)

        sel.deselect_all()
        time.sleep(2)

        #printing the option's text

        dropdown.select_by_value("option 1")

        dropdown.select_by_value("option 3")
        time.sleep(2)
        print("Selected Options:")
        for option in dropdown.all_selected_options:
            print(option.text)

        driver.quit()

