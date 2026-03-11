"""
conftest.py

This file contains:
1. WebDriver setup fixture
2. Global configuration for tests
3. Screenshot capture on test failure

Used Concepts:
 Pytest Fixtures
 Selenium WebDriver setup
 Implicit Wait
 Screenshot Hook
 Reusable driver across test classes
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import time
from datetime import datetime


# ---------------- DRIVER FIXTURE ---------------- #

@pytest.fixture(scope="function")
def driver(request):
    """
    This fixture initializes the Chrome WebDriver
    and makes it available to all tests.

    Scope = function (new browser per test)
    """

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Maximize browser window
    driver.maximize_window()

    # Implicit wait (global wait)
    driver.implicitly_wait(10)

    # Open application
    driver.get("https://bstackdemo.com/")

    # Attach driver to test class
    request.cls.driver = driver

    yield driver

    # Close browser after test execution
    driver.quit()


# ---------------- DEMO DELAY (OPTIONAL) ---------------- #

@pytest.fixture(autouse=True)
def slow_demo():
    """
    Small delay between actions so automation
    can be clearly visible during demonstration.
    """
    time.sleep(3)


# ---------------- SCREENSHOT HOOK ---------------- #

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture screenshot when test fails.
    """

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # timestamp for unique screenshot name
            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

            file_path = os.path.join(screenshots_dir, file_name)

            # capture screenshot
            driver.save_screenshot(file_path)

            print(f"\nScreenshot saved at: {file_path}")

