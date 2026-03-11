import os
import time
import pytest
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.order_confirmation_page import OrderConfirmationPage
from Utilities.logger import get_logger
from Utilities.excel_utils import get_excel_data


"""
Test Data Setup
Reads shipping information and products names from Excel file for data-driven testing
"""
test_data = get_excel_data(
    "/Users/arunkumartepan/Desktop/Selenium_Pytes_POM/BStackDemo Selenium Automation Framework/Testdata/Shipping_Info.xlsx",
    "Sheet1"
)
products = get_excel_data(
    "/Users/arunkumartepan/Desktop/Selenium_Pytes_POM/BStackDemo Selenium Automation Framework/Testdata/Products.xlsx",
    "Sheet1"
)
# Initialize Logger
logger = get_logger()

# Expected location where the order receipt will be downloaded
DOWNLOAD_PATH = "/Users/arunkumartepan/Downloads/confirmation.pdf"


@pytest.mark.usefixtures("driver")
class TestOrderConfirmation:

    """
    End-to-End Order Confirmation Test Suite

    Flow Covered:
    Login → Product Search → Add Products → Cart Validation
    → Checkout → Download Receipt → Continue Shopping
    """

    # ---------------------------------------------------------
    # LOGIN TEST
    # ---------------------------------------------------------
    def test_login(self, driver):

        try:
            logger.info("Logging in using Demo User")

            lp = LoginPage(driver)
            lp.login(lp.DEMO_USER)

            time.sleep(2)

            logger.info("Login successful")

        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            pytest.fail("Login Test Failed")


    # ---------------------------------------------------------
    # ADD PRODUCTS TO CART
    # ---------------------------------------------------------
    def test_add_products(self, driver):

        try:
            # Ensure user is logged in before adding products
            self.test_login(driver)
            """
                   Test searching products from Excel
                   and adding them to cart.
                   """

            product_page = ProductPage(driver)

            for product in products:
                product_name = product[0]

                # Log current product being tested
                print(f"\nSearching product: {product_name}")

                # Step 1: Search product
                product_page.search_product(product_name)

                # Step 2: Click search button
                product_page.click_search()

                time.sleep(2)

                # Step 3: Add product to cart
                product_page.add_product_to_cart(product_name)

                time.sleep(2)

            print("\nAll products added successfully")

        except Exception as e:
            logger.error(f"Adding products failed: {str(e)}")
            pytest.fail("Add Products Test Failed")


    # ---------------------------------------------------------
    # CART VALIDATION
    # ---------------------------------------------------------
    def test_validate_cart(self, driver):

        try:
            # Execute previous steps
            self.test_add_products(driver)

            cart = CartPage(driver)

            logger.info("Opening cart")
            cart.open_cart()

            time.sleep(2)

            logger.info("Validating products inside cart")
            products = cart.get_cart_products()

            assert "iPhone 12" in products
            assert "One Plus 6T" in products

            logger.info("Validating subtotal value")
            subtotal = cart.get_subtotal()

            assert "1228" in subtotal

        except Exception as e:
            logger.error(f"Cart validation failed: {str(e)}")
            pytest.fail("Cart Validation Test Failed")


    # ---------------------------------------------------------
    # CHECKOUT PROCESS
    # ---------------------------------------------------------
    @pytest.mark.parametrize("firstname, lastname, address, state, postalcode", test_data)
    def test_checkout(self, driver, firstname, lastname, address, state, postalcode):

        try:
            # Execute previous steps
            self.test_validate_cart(driver)

            cart = CartPage(driver)

            logger.info("Clicking checkout button")
            cart.click_checkout()

            time.sleep(2)

            checkout = CheckoutPage(driver)

            logger.info("Entering shipping details")

            checkout.enter_first_name(firstname)
            checkout.enter_last_name(lastname)
            checkout.enter_address(address)
            checkout.enter_state(state)
            checkout.enter_postal_code(postalcode)

            checkout.click_submit()

        except Exception as e:
            logger.error(f"Checkout failed: {str(e)}")
            pytest.fail("Checkout Test Failed")


    # ---------------------------------------------------------
    # DOWNLOAD RECEIPT
    # ---------------------------------------------------------
    @pytest.mark.parametrize("firstname, lastname, address, state, postalcode", test_data)
    def test_download_receipt(self, driver, firstname, lastname, address, state, postalcode):

        try:
            # Execute checkout flow
            self.test_checkout(driver, firstname, lastname, address, state, postalcode)

            oc = OrderConfirmationPage(driver)

            logger.info("Downloading receipt")
            oc.click_download_receipt()

            time.sleep(5)

            logger.info("Validating receipt download")

            if not oc.is_receipt_downloaded(DOWNLOAD_PATH):
                pytest.fail("Receipt not downloaded")

        except Exception as e:
            logger.error(f"Receipt download failed: {str(e)}")
            pytest.fail("Receipt Download Test Failed")


    # ---------------------------------------------------------
    # CONTINUE SHOPPING
    # ---------------------------------------------------------
    @pytest.mark.parametrize("firstname, lastname, address, state, postalcode", test_data)
    def test_continue_shopping(self, driver, firstname, lastname, address, state, postalcode):

        try:
            # Execute full flow until receipt download
            self.test_download_receipt(driver, firstname, lastname, address, state, postalcode)

            oc = OrderConfirmationPage(driver)

            logger.info("Clicking continue shopping")

            oc.click_continue_shopping()

            time.sleep(2)

            logger.info("Validating user returned to home page")

            assert "StackDemo" in driver.page_source

        except Exception as e:
            logger.error(f"Continue shopping failed: {str(e)}")
            pytest.fail("Continue Shopping Test Failed")