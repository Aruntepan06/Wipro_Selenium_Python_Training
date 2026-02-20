*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php

*** Test Cases ***
Select State And City
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    id=state

    # Select State
    Select From List By Label    id=state    Uttar Pradesh
    Sleep    2s

    # Wait for City dropdown to load
    Wait Until Element Is Visible    id=city

    # Select City
    Select From List By Label    id=city    Lucknow
    Sleep    2s

    Close Browser
