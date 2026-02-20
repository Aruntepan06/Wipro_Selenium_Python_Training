*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://practice.automationtesting.in/

*** Test Cases ***
Complete Purchase Flow
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # Scroll to products
    Execute JavaScript    window.scrollTo(0,600)

    # Add Selenium Ruby to cart
    Click Element    xpath://h3[text()='Selenium Ruby']/ancestor::li//a[contains(@class,'add_to_cart_button')]
    Sleep    2s

    # Go to Basket directly (stable)
    Go To    https://practice.automationtesting.in/basket/

    # Proceed to Checkout
    Wait Until Element Is Visible    css:a.checkout-button
    Click Element    css:a.checkout-button

    # Fill Billing Details

    Wait Until Element Is Visible    id=billing_first_name

    Input Text    id=billing_first_name    TestFirst
    Sleep    3s
    Input Text    id=billing_last_name     TestLast
    Sleep    4s
    Input Text    id=billing_email         test123@testmail.com
    Sleep    4s
    Input Text    id=billing_phone         9876543210
    Sleep    4s

    Input Text    id=billing_address_1     123 Automation Street
    Sleep    4s
    Input Text    id=billing_city          Hyderabad
    Sleep    4s

    Select From List By Label    id=billing_state    Telangana
    Input Text    id=billing_postcode      500001
    Sleep    4s

    # Order Notes
    Input Text    id=order_comments        This is automation test order

    Sleep    4s

    #Place Order
    Scroll Element Into View    id=place_order
    Click Element               id=place_order

    Sleep    5s
    Close Browser