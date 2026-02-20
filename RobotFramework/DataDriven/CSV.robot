*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=/Users/arunkumartepan/PycharmProjects/RobotFramework/TestData/ddtLogindataCSV.csv
Test Template    Login Test
Test Setup    Setup Browser
Test Teardown    Close Browser

*** Test Cases ***
Login with user    ${username}    ${password}

*** Keywords ***
Setup Browser
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

Login Test
    [Arguments]    ${username}    ${password}

    Wait Until Page Contains Element    xpath://input[@name='username']    20s
    Wait Until Element Is Visible       xpath://input[@name='username']    20s

    Clear Element Text    xpath://input[@name='username']
    Input Text            xpath://input[@name='username']    ${username}

    Clear Element Text    xpath://input[@name='password']
    Input Text            xpath://input[@name='password']    ${password}

    Click Element         xpath://button[@type='submit']

    Wait Until Page Contains Element    xpath://h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']    20s
    Element Should Be Visible           xpath://h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']