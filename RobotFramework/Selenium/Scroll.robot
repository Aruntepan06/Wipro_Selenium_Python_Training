*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify Sell On Amazon Page
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://a[contains(.,'Sell on Amazon')]    20s
    Scroll Element Into View    xpath://a[contains(.,'Sell on Amazon')]
    Click Element    xpath://a[contains(.,'Sell on Amazon')]

    Wait Until Page Contains    Start Selling Now    20s
    Page Should Contain    Start Selling Now

    Close Browser