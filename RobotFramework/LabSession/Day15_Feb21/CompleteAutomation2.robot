*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}             https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}         chrome
${VALID_USER}      Admin
${VALID_PASS}      admin123
${INVALID_PASS}    wrongpass123
${ERROR_MSG}       Invalid credentials

*** Test Cases ***
TC_01_Verify Successful Employee Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@name='username']    10s

    Input Text    xpath://input[@name='username']    ${VALID_USER}
    Input Text    xpath://input[@name='password']    ${VALID_PASS}
    Click Button    xpath://button[@type='submit']

    Wait Until Element Is Visible    xpath://h6[text()='Dashboard']    10s
    Element Should Be Visible        xpath://h6[text()='Dashboard']

    Close Browser


TC_02_Verify Error Message On Unsuccessful Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@name='username']    10s

    Input Text    xpath://input[@name='username']    ${VALID_USER}
    Input Text    xpath://input[@name='password']    ${INVALID_PASS}
    Click Button    xpath://button[@type='submit']

    Wait Until Element Is Visible    xpath://p[contains(@class,'oxd-alert-content-text')]    10s
    Element Text Should Be           xpath://p[contains(@class,'oxd-alert-content-text')]    ${ERROR_MSG}
    Page Should Not Contain Element  xpath://h6[text()='Dashboard']

    Close Browser