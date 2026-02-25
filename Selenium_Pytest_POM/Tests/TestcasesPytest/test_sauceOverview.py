import time
import pytest

from test_saucelogin import LoginPage
from Pages.sauceAddProduct_page import SauceAddProductPage
from Pages.sauceCart_Page import SauceCart
from Pages.sauce_userinfo import USER_INFO
from Pages.sauce_CheckoutOverview import CheckoutOverview   # change import if your file name is different
from Utilities.logger import get_logger
from Utilities.excel_utils import get_excel_data

test_data = get_excel_data(
    "/Users/arunkumartepan/PycharmProjects/Feb_2026_Selenium_Pytest_POM/Testdata/login_data.xlsx",
    "Sheet1"
)

test_data2 = get_excel_data(
    "/Users/arunkumartepan/PycharmProjects/Feb_2026_Selenium_Pytest_POM/Testdata/test_data2.xlsx",
    "Sheet1"
)

loger = get_logger()

@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.mark.parametrize("username, password", test_data)
    @pytest.mark.parametrize("first_name, last_name, postal_code", test_data2)
    def test_login_addprod_checkout_form_excel(self, driver, username, password, first_name, last_name, postal_code):

        loger.info("Opening application")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        lp = LoginPage(driver)
        lp.login(username, password)

        if password == "secret_sauce":
            assert "Swag Labs" in driver.title
        else:
            assert "Invalid credentials" in lp.get_error_message()
            return

        sp = SauceAddProductPage(driver)
        sp.add_prod()
        time.sleep(1)

        sp.open_cart()
        time.sleep(1)
        assert sp.get_cart_title() == "Your Cart"

        sc = SauceCart(driver)
        sc.checkout()
        time.sleep(1)

        ui = USER_INFO(driver)
        ui.form(first_name, last_name, postal_code)
        time.sleep(3)
        ui.conbtn()
        time.sleep(3)

        co = CheckoutOverview(driver)
        assert co.get_page_title() == "Checkout: Overview"
        co.click_finish()
        time.sleep(2)