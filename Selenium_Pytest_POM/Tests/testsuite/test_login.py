#check the title of the web page

import pytest
from Pages.Login_page import LoginPage


# @pytest.mark.usefixtures("driver")
# class TestLogin:
#
#     def test_title(self):
#         print(self.driver.title)
#         assert "OrangeHRM" in self.driver.title
#
#     def test_validate(self, driver):
#         lp = LoginPage(driver)
#         lp.login("Admin", "admin123")
#         assert "OrangeHRM" in driver.title

# @pytest.mark.usefixtures("driver")
# class TestLogin:
#
#     def test_validate(self, driver):
#         lp = LoginPage(driver)
#         lp.login("standard_user", "secret_sauce")
#         assert "Swag Labs" in driver.title