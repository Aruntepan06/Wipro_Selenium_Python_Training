*** Settings ***
# setting we add the external library details, resources, set up and tear down commands
# Suite Setup runs once before all tests
# Suite Teardown runs once after all tests

Resource        ./../Resources/Resource.robot
Library         SeleniumLibrary
Suite Setup     Launch Open_DB
Suite Teardown  Launch Close_DB


*** Test Cases ***
Verify login with valid credentials
    Login

Verify Add to cart functionality
    Login
    Log    User selects the product
    Log    User adds the product to the cart
    Log    User verifies that the product with details is added to the cart
