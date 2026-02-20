*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window

    # wait till the element is loaded
    Sleep    3s
    Wait Until Element Is Visible    xpath://input[@id='file-upload']

    # capture page screen shot
    Capture Page Screenshot    /Users/arunkumartepan/Downloads/sampleFile1.png

    # capture element screen shot
    Capture Element Screenshot    xpath://input[@id='file-upload']    /Users/arunkumartepan/Downloads/sampleFile2.png

    Sleep    2s
    # close browser
    Close Browser