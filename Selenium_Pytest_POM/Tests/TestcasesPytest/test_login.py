#check the title of the web page
import time

import pytest
from Pages.Login_page import LoginPage
from Utilities.logger import get_logger
from Utilities.excel_utils import get_excel_data
test_data = get_excel_data("/Users/arunkumartepan/PycharmProjects/Feb_2026_Selenium_Pytest_POM/Testdata/login_data.xlsx","Sheet1")
loger = get_logger()

loger = get_logger()

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_validate(self, driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep((3))
        loger.info("Opening the Browser")
        lp = LoginPage(driver)
        lp.login("Admin", "admin123")
        time.sleep((3))
        loger.info("Entering the Credentials")
        assert "OrangeHRM" in driver.title

    def test_invalid_login(self, driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep((3))
        loger.info("Opening the Browser")
        lp = LoginPage(driver)
        lp.login("Admin", "AAdmin123")
        time.sleep((3))
        loger.info("Entering the Credentials")
        assert"Invalid credentials" in lp.get_error_message()

    # test data stored in excel sheet
    @pytest.mark.parametrize("username, password", test_data)
    def test_login_excel(self, driver, username, password):
        loger.info("Opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        # create the object of login_page
        lp = LoginPage(driver)
        lp.login(username, password)

        if password == "admin123":
            assert "OrangeHRM" in driver.title
        else:
            assert "Invalid credentials" in lp.get_error_message()
