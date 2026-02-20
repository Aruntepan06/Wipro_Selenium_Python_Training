*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify multiselect check boxs
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window
    # identify the common elements attribute - //input[@type = 'checkbox']
    ${elements}=    Get WebElements    xpath://input[starts-with(@id,'c_bs_')]
    FOR    ${element}    IN    @{elements}
        Click Element    ${element}
        Sleep    2s
    END
    # close browser
    Close Browser
