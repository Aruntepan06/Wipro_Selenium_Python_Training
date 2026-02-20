*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Open Window
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    Click Element    id=openwindow

    Switch Window    NEW
    Sleep    2s


    ${title}=    Get Title
    Log To Console    ${title}

    Close Window
    Switch Window    MAIN
    Close Browser