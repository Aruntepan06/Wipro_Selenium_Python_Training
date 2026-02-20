*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Verify Alerts
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Click Element    xpath=(//button)[1]
    Handle Alert    ACCEPT    timeout=5s
    Sleep    5s

    Click Element    xpath=(//button)[2]
    Handle Alert    DISMISS    timeout=5s
    Sleep    5s

    Click Element    xpath=(//button)[3]
    Input Text Into Alert    Hello

    Close Browser
