*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL}            https://www.tutorialspoint.com/selenium/practice/upload-download.php
${DOWNLOAD_PATH}  /Users/arunkumartepan/Downloads/sampleFile.png

*** Test Cases ***
Verify Download And Upload
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    # Download file
    Click Element    id=downloadButton
    Sleep    5s
    File Should Exist    ${DOWNLOAD_PATH}

    # Upload file
    Choose File    id=uploadFile    ${DOWNLOAD_PATH}

    # Validate upload
    ${value}=    Get Element Attribute    id=uploadFile    value
    #Should Contain    ${value}    sampleFile.jpeg

    Sleep    3s
    Close Browser