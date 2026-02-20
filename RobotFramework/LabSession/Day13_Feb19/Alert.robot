*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/alerts.php



*** Test Cases ***
Verify Alerts
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        Wait Until Element Is Visible    xpath=//button[normalize-space()='Alert']
        Click Element    xpath://button[normalize-space()='Alert']
        # Informational alert - accept is for ok btn
        Handle Alert        action=ACCEPT       timeout=3
        Sleep    5s

        Click Element    xpath://button[@onclick='myDesk()']
        # Conformational alert - accept is for ok btn dismiss for cancel
        Handle Alert        action=DISMISS       timeout=3
        Sleep    5s
        #promt alert accept is for ok btn dismiss for cancel
        Click Element    xpath://button[@onclick='myPromp()']
        Input Text Into Alert    Hello
        Sleep    5s



        Close Browser