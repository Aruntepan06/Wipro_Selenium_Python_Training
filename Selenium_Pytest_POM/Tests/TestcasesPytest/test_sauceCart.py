import time

import pytest
from test_saucelogin import LoginPage
from Pages.sauceAddProduct_page import SauceAddProductPage
from Pages.sauceCart_Page import SauceCart
from Utilities.logger import get_logger
from Utilities.excel_utils import get_excel_data
test_data = get_excel_data("/Users/arunkumartepan/PycharmProjects/Feb_2026_Selenium_Pytest_POM/Testdata/login_data.xlsx","Sheet1")
loger = get_logger()

loger = get_logger()

@pytest.mark.usefixtures("driver")
class TestLogin:
    # test data stored in excel sheet
    @pytest.mark.parametrize("username, password", test_data)
    def test_login_excel(self, driver, username, password):
        loger.info("Opening application")
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        # create the object of login_page
        lp =LoginPage(driver)
        lp.login(username, password)
        if password == "secret_sauce":
            assert "Swag Labs" in driver.title

        else:
            assert "Invalid credentials" in lp.get_error_message()

        sp = SauceAddProductPage(driver)
        sp.add_prod()  # adding the products
        time.sleep(3)
        sp.open_cart()  #opening the cart after adding the product
        time.sleep(3)
        assert sp.get_cart_title() == "Your Cart"
        sc=SauceCart(driver)
        sc.checkout()    # Clicking on checkout after reviewing the products
        time.sleep(3)






