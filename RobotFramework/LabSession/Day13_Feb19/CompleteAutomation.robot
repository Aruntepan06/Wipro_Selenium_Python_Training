*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.saucedemo.com/

*** Test Cases ***
Checkout Step One
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Sleep    2s

    # Login
    Input Text    id=user-name    standard_user
    Sleep    5s
    Input Text    id=password     secret_sauce
    Sleep    5s
    Click Button  id=login-button
    Sleep    5s

    # Add item
    Click Button    id=add-to-cart-sauce-labs-backpack
    Sleep    5s

    # Go to cart
    Click Element    class=shopping_cart_link
    Sleep    5s

    # Checkout
    Click Button    id=checkout
    Sleep    5s

    # Fill details
    Input Text    id=first-name    Arun
    Sleep    5s
    Input Text    id=last-name     Tepan
    Sleep    5s
    Input Text    id=postal-code   303007
    Sleep    5s

    # Click Continue
    Click Button    id=continue
    Sleep    5s
    # Click Finish
    Click Button    id=finish
    Sleep    5s
    Element Should Contain    class=complete-text    Your order has been dispatched
    Sleep    5s



    Close Browser
