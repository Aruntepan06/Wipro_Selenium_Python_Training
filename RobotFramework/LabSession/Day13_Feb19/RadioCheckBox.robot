*** Settings ***
Library    SeleniumLibrary
Library    XML

*** Variables ***
${radio_url}    https://www.tutorialspoint.com/selenium/practice/radio-button.php
${check_url}    https://www.tutorialspoint.com/selenium/practice/check-box.php


*** Test Cases ***
Verify radio and check box
    Open Browser    ${radio_url}    chrome
    # maximize the browser window
    Maximize Browser Window
    # wait till the element is loaded

    Wait Until Element Is Visible    xpath://input[@value='igottwo']
    # click on radio button
    Click Element    xpath://input[@value='igottwo']
    Sleep    2s
    #click on check_box option
    Go To    ${check_url}
    Click Element    xpath://input[@id='c_bs_2']
    Sleep    3s
    # close browser
    Close Browser
