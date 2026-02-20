*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window

    # wait till the element is loaded
    Sleep    3s
    Wait Until Element Is Visible    xpath://div[@id='draggable']
    Sleep    4s
    Drag And Drop    xpath://div[@id='draggable']    xpath://div[@id='droppable']

    Sleep    2s
    # close browser
    Close Browser