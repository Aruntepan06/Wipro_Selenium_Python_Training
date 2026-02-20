** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/



*** Test Cases ***
Verify Alerts
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        Wait Until Element Is Visible    xpath=//input[@id='alertbtn']
        Click Element    xpath://input[@id='alertbtn']
        # Informational alert - accept is for ok btn
        Handle Alert        action=ACCEPT       timeout=3
        Sleep    5s

        Click Element    xpath://input[@id='confirmbtn']
        # Conformational alert - accept is for ok btn dismiss for cancel
        Handle Alert        action=DISMISS       timeout=3
        Sleep    5s



        Close Browser