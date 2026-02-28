import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

# Locators
HOME_BTN = (By.XPATH, "//button[normalize-space()='Home']")
CUSTOMER_LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Customer Login']")
BANK_MANAGER_BTN = (By.XPATH, "//button[normalize-space()='Bank Manager Login']")

ADD_CUSTOMER_TAB = (By.XPATH, "//button[normalize-space()='Add Customer']")
FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
POST_CODE = (By.XPATH, "//input[@placeholder='Post Code']")
ADD_CUSTOMER_BTN = (By.XPATH, "//button[@type='submit']")

OPEN_ACCOUNT_TAB = (By.XPATH, "//button[normalize-space()='Open Account']")
CUSTOMER_SELECT = (By.XPATH, "//select[@id='userSelect']")
CURRENCY_SELECT = (By.XPATH, "//select[@id='currency']")
PROCESS_BTN = (By.XPATH, "//button[normalize-space()='Process']")

LOGIN_BTN = (By.XPATH, "//button[@type='submit' and normalize-space()='Login']")
CUSTOMER_NAME_TXT = (By.XPATH, "//span[@class='fontBig ng-binding']")

DEPOSIT_TAB = (By.XPATH, "//button[normalize-space()='Deposit']")
WITHDRAWL_TAB = (By.XPATH, "//button[normalize-space()='Withdrawl']")
AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='amount']")
DEPOSIT_BTN = (By.XPATH, "//button[@type='submit' and normalize-space()='Deposit']")
WITHDRAW_BTN = (By.XPATH, "//button[@type='submit' and normalize-space()='Withdraw']")

# Message sometimes has different classes, so use contains
MSG = (By.XPATH, "//span[contains(@class,'ng-binding') and (contains(@class,'error') or contains(@class,'ng-scope'))]")

# Balance is the 2nd strong in the center header line
BALANCE_VALUE = (By.XPATH, "(//div[contains(@class,'center')]//strong[contains(@class,'ng-binding')])[2]")


def rand_letters(n: int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(n)).capitalize()


def rand_digits(n: int) -> str:
    return "".join(random.choice(string.digits) for _ in range(n))


@pytest.fixture
def driver():
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    d.maximize_window()
    yield d
    d.quit()


def click(wait: WebDriverWait, locator):
    wait.until(EC.element_to_be_clickable(locator)).click()


def type_text(wait: WebDriverWait, locator, text: str):
    el = wait.until(EC.visibility_of_element_located(locator))
    el.clear()
    el.send_keys(text)


def select_by_label(wait: WebDriverWait, locator, label: str):
    el = wait.until(EC.visibility_of_element_located(locator))
    Select(el).select_by_visible_text(label)


def accept_alert(wait: WebDriverWait):
    alert = wait.until(EC.alert_is_present())
    alert.accept()


def get_int_text(wait: WebDriverWait, locator) -> int:
    txt = wait.until(EC.visibility_of_element_located(locator)).text.strip()
    return int(txt)


def wait_msg_contains(wait: WebDriverWait, expected_substring: str) -> str:
    el = wait.until(EC.visibility_of_element_located(MSG))
    text = el.text.strip()
    assert expected_substring in text
    return text


@pytest.mark.order(1)
def test_xyzbank_end_to_end(driver):
    wait = WebDriverWait(driver, 20)
    driver.get(URL)
    time.sleep(1.5)

    # Random customer data every run
    first = rand_letters(6)
    last = rand_letters(6)
    post = rand_digits(6)
    full_name = f"{first} {last}"

    # Bank Manager -> Add Customer
    click(wait, BANK_MANAGER_BTN)
    time.sleep(1.5)

    click(wait, ADD_CUSTOMER_TAB)
    time.sleep(1.5)

    type_text(wait, FIRST_NAME, first)
    time.sleep(1)
    type_text(wait, LAST_NAME, last)
    time.sleep(1)
    type_text(wait, POST_CODE, post)
    time.sleep(1)

    click(wait, ADD_CUSTOMER_BTN)
    time.sleep(1)
    accept_alert(wait)
    time.sleep(1.5)

    # Open Account for that customer
    click(wait, OPEN_ACCOUNT_TAB)
    time.sleep(1.5)

    select_by_label(wait, CUSTOMER_SELECT, full_name)
    time.sleep(1)

    select_by_label(wait, CURRENCY_SELECT, "Dollar")
    time.sleep(1)

    click(wait, PROCESS_BTN)
    time.sleep(1)
    accept_alert(wait)
    time.sleep(1.5)

    # Home -> Customer Login -> select name -> validate customer name
    click(wait, HOME_BTN)
    time.sleep(1.5)

    click(wait, CUSTOMER_LOGIN_BTN)
    time.sleep(1.5)

    select_by_label(wait, CUSTOMER_SELECT, full_name)
    time.sleep(1)

    click(wait, LOGIN_BTN)
    time.sleep(1.5)

    shown_name = wait.until(EC.visibility_of_element_located(CUSTOMER_NAME_TXT)).text.strip()
    assert shown_name == full_name

    # Deposit
    before = get_int_text(wait, BALANCE_VALUE)

    dep_amt = int(rand_digits(5))  # random deposit amount
    click(wait, DEPOSIT_TAB)
    time.sleep(1.2)

    type_text(wait, AMOUNT_INPUT, str(dep_amt))
    time.sleep(1)

    click(wait, DEPOSIT_BTN)
    wait_msg_contains(wait, "Deposit Successful")
    time.sleep(1.5)

    after_dep = get_int_text(wait, BALANCE_VALUE)
    assert after_dep == before + dep_amt

    # Withdraw
    wd_amt = int(rand_digits(4))  # random withdraw amount
    click(wait, WITHDRAWL_TAB)
    time.sleep(1.2)

    type_text(wait, AMOUNT_INPUT, str(wd_amt))
    time.sleep(1)

    click(wait, WITHDRAW_BTN)
    wait_msg_contains(wait, "Transaction successful")
    time.sleep(1.5)

    after_wd = get_int_text(wait, BALANCE_VALUE)
    assert after_wd == after_dep - wd_amt

    # Finally Home
    click(wait, HOME_BTN)
    time.sleep(1.5)