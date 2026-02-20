*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/frames.php

*** Test Cases ***
Identify And Print Frame Text
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # Switch to Iframe 1
    Select Frame    xpath:(//iframe)[1]

    # Get text inside frame
    ${text}=    Get Text    xpath://body
    Log To Console    ${text}

    # Go back to main page
    Unselect Frame

    # Switch to Iframe 2
    Select Frame    xpath:(//iframe)[2]

    ${text2}=    Get Text    xpath://body
    Log To Console    ${text2}

    Unselect Frame
    Close Browser