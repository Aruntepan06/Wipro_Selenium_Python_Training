*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}              https://the-internet.herokuapp.com/upload
${Path_DIR}     /Users/arunkumartepan/Downloads/sampleFile.png
*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window
    # wait till the element is loaded
    Sleep    3s
    Wait Until Element Is Visible    xpath://input[@id='file-upload']
    Choose File    xpath://input[@id='file-upload']    ${Path_DIR}
    # click the upload button
    Click Element    xpath://input[@id='file-submit']
    Sleep    2s
    Element Should Be Visible    xpath://h3[normalize-space()='File Uploaded!']
    Element Text Should Be    xpath://h3[normalize-space()='File Uploaded!']    File Uploaded!
    Sleep    2s
    # close browser
    Close Browser