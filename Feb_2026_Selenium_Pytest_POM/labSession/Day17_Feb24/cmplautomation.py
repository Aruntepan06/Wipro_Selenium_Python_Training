import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_Register_Login_AddToCart_Checkout:

    def test_flow(self):

        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Open Demo Web Shop website
        driver.get("https://demowebshop.tricentis.com/")
        time.sleep(2)

        # Generate random user details
        first_name = ''.join(random.choices(string.ascii_letters, k=6))
        last_name = ''.join(random.choices(string.ascii_letters, k=6))
        email = f"{first_name.lower()}{random.randint(1000,9999)}@test.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # Click on Register link
        driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)

        # Fill registration form
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(first_name)
        driver.find_element(By.ID, "LastName").send_keys(last_name)
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
        time.sleep(2)

        # Click Register button
        driver.find_element(By.ID, "register-button").click()
        time.sleep(3)

        # Click Continue after successful registration
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "register-continue-button"))).click()
        time.sleep(2)

        # Logout after registration
        driver.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(2)

        # Click on Login link
        driver.find_element(By.LINK_TEXT, "Log in").click()
        time.sleep(2)

        # Enter login credentials
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        time.sleep(2)

        # Click Login button
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        time.sleep(3)

        # Validate successful login
        assert "Log out" in driver.page_source

        # Scroll down to Featured Products
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Add Featured Product to cart (14.1-inch Laptop)
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//h2[@class='product-title']/a[contains(text(),'14.1-inch Laptop')]/ancestor::div[contains(@class,'product-item')]//input[contains(@class,'product-box-add-to-cart-button')]"
        )))
        add_to_cart_btn.click()
        time.sleep(3)

        # Scroll up and click Shopping cart
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='ico-cart' and contains(@href,'/cart')]"))).click()
        time.sleep(3)

        # Validate Shopping cart page opened
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Shopping cart']")))
        assert header.is_displayed()

        # Accept terms of service
        tos_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        if not tos_checkbox.is_selected():
            tos_checkbox.click()
        time.sleep(1)

        # Click Checkout button
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        time.sleep(3)

        # Validate Checkout page opened
        checkout_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Checkout']")))
        assert checkout_header.is_displayed()

        # Generate random billing address details
        company = "Comp" + str(random.randint(100, 999))
        city = "City" + str(random.randint(10, 99))
        address1 = str(random.randint(10, 999)) + " Street"
        zip_code = str(random.randint(100000, 999999))
        phone = str(random.randint(7000000000, 9999999999))

        # Fill Billing Address form
        fn = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        fn.clear()
        fn.send_keys(first_name)

        ln = driver.find_element(By.ID, "BillingNewAddress_LastName")
        ln.clear()
        ln.send_keys(last_name)

        em = driver.find_element(By.ID, "BillingNewAddress_Email")
        em.clear()
        em.send_keys(email)

        comp = driver.find_element(By.ID, "BillingNewAddress_Company")
        comp.clear()
        comp.send_keys(company)

        # Select Country
        country_dd = Select(driver.find_element(By.ID, "BillingNewAddress_CountryId"))
        country_dd.select_by_visible_text("United States")
        time.sleep(2)

        # Select State
        state_dd = Select(wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))))
        state_dd.select_by_index(1)
        time.sleep(1)

        cty = driver.find_element(By.ID, "BillingNewAddress_City")
        cty.clear()
        cty.send_keys(city)

        addr1 = driver.find_element(By.ID, "BillingNewAddress_Address1")
        addr1.clear()
        addr1.send_keys(address1)

        postal = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        postal.clear()
        postal.send_keys(zip_code)

        ph = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        ph.clear()
        ph.send_keys(phone)

        time.sleep(2)

        # Click Continue on Billing Address
        wait.until(EC.element_to_be_clickable((
            By.XPATH, "//input[@type='button' and @value='Continue' and contains(@class,'new-address-next-step-button')]"
        ))).click()

        time.sleep(3)
        driver.quit()