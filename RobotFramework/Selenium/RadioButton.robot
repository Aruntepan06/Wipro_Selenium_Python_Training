*** Settings ***
Library    SeleniumLibrary
Library    XML

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window
    # wait till the element is loaded
    
    Wait Until Element Is Visible    xpath://input[@value = 'radio1']
    # click on radio button
    Click Element    xpath://input[@value = 'radio1']
    #click on check_box option 3
    Sleep    5s
    Click Element    id=checkBoxOption3
    Sleep    3s
    # close browser
    Close Browser
