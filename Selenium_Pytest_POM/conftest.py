from selenium import webdriver
import pytest
import os
import time
from datetime import datetime
# @pytest.fixture(scope="function")
# def driver(request):
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     #driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
#
# # screen shot hook taking if the test case fails
@pytest.hookimpl(hookwrapper=True)
# screen shot hook taking if the test case fails
def pytest_runtest_makereport(item , call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir , exist_ok = True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )

    yield driver
    driver.quit()
