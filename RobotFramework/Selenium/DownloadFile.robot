*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}              https://the-internet.herokuapp.com/download
${DOWNLOAD_DIR}     /Users/arunkumartepan/Downloads

*** Test Cases ***
Verify File Download Link
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://a[normalize-space()='sample-zip-file.zip']
    Click Element    xpath://a[normalize-space()='sample-zip-file.zip']

    Wait Until Keyword Succeeds    10x    1s
    ...    File Should Exist    ${DOWNLOAD_DIR}/sample-zip-file.zip

    ${files}=    List Files In Directory    ${DOWNLOAD_DIR}
    List Should Contain Value    ${files}    sample-zip-file.zip

    Close Browser
