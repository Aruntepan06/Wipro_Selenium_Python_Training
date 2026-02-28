*** Settings ***
Library    SeleniumLibrary
Library    String

Suite Setup       Open XYZ Bank
Suite Teardown    Close All Browsers

*** Variables ***
${URL}      https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
${BROWSER}  chrome
${WAIT}     2s

${HOME_BTN}            //button[normalize-space()='Home']
${CUSTOMER_LOGIN_BTN}  //button[normalize-space()='Customer Login']
${BANK_MANAGER_BTN}    //button[normalize-space()='Bank Manager Login']

${ADD_CUSTOMER_TAB}    //button[normalize-space()='Add Customer']
${FIRST_NAME}          //input[@placeholder='First Name']
${LAST_NAME}           //input[@placeholder='Last Name']
${POST_CODE}           //input[@placeholder='Post Code']
${ADD_CUSTOMER_BTN}    //button[@type='submit']

${OPEN_ACCOUNT_TAB}    //button[normalize-space()='Open Account']
${CUSTOMER_SELECT}     //select[@id='userSelect']
${CURRENCY_SELECT}     //select[@id='currency']
${PROCESS_BTN}         //button[normalize-space()='Process']

${USER_SELECT}         //select[@id='userSelect']
${LOGIN_BTN}           //button[@type='submit' and normalize-space()='Login']
${CUSTOMER_NAME_TXT}   //span[@class='fontBig ng-binding']

${DEPOSIT_TAB}         //button[normalize-space()='Deposit']
${WITHDRAWL_TAB}       //button[normalize-space()='Withdrawl']
${AMOUNT_INPUT}        //input[@placeholder='amount']
${DEPOSIT_BTN}         //button[@type='submit' and normalize-space()='Deposit']
${WITHDRAW_BTN}        //button[@type='submit' and normalize-space()='Withdraw']

# FIX: message xpath should match both success/error cases (sometimes class differs)
${MSG}                 //span[contains(@class,'ng-binding') and (contains(@class,'error') or contains(@class,'ng-scope'))]

${BALANCE_VALUE}       (//div[contains(@class,'center')]//strong[contains(@class,'ng-binding')])[2]


*** Test Cases ***
End To End - Add Customer Open Account Deposit Withdraw Validate Balance
    Click Element    ${BANK_MANAGER_BTN}
    Sleep    ${WAIT}

    Click Element    ${ADD_CUSTOMER_TAB}
    Sleep    ${WAIT}

    ${RAND_FIRST}=    Generate Random String    6    [LETTERS]
    ${RAND_LAST}=     Generate Random String    6    [LETTERS]
    ${RAND_POST}=     Generate Random String    6    [NUMBERS]
    ${FULL_NAME}=     Set Variable    ${RAND_FIRST} ${RAND_LAST}

    Input Text    ${FIRST_NAME}    ${RAND_FIRST}
    Sleep    ${WAIT}
    Input Text    ${LAST_NAME}     ${RAND_LAST}
    Sleep    ${WAIT}
    Input Text    ${POST_CODE}     ${RAND_POST}
    Sleep    ${WAIT}

    Click Element    ${ADD_CUSTOMER_BTN}
    Sleep    ${WAIT}
    Handle Alert    action=ACCEPT
    Sleep    ${WAIT}

    Click Element    ${OPEN_ACCOUNT_TAB}
    Sleep    ${WAIT}

    Wait Until Element Is Visible    ${CUSTOMER_SELECT}    10
    Select From List By Label    ${CUSTOMER_SELECT}    ${FULL_NAME}
    Sleep    ${WAIT}

    Select From List By Label    ${CURRENCY_SELECT}    Dollar
    Sleep    ${WAIT}

    Click Element    ${PROCESS_BTN}
    Sleep    ${WAIT}
    Handle Alert    action=ACCEPT
    Sleep    ${WAIT}

    Click Element    ${HOME_BTN}
    Sleep    ${WAIT}

    Click Element    ${CUSTOMER_LOGIN_BTN}
    Sleep    ${WAIT}

    Wait Until Element Is Visible    ${USER_SELECT}    10
    Select From List By Label    ${USER_SELECT}    ${FULL_NAME}
    Sleep    ${WAIT}

    Click Element    ${LOGIN_BTN}
    Sleep    ${WAIT}

    Element Text Should Be    ${CUSTOMER_NAME_TXT}    ${FULL_NAME}
    Sleep    ${WAIT}

    ${before}=    Get Balance

    ${DEP_AMT_TXT}=    Generate Random String    5    [NUMBERS]
    ${DEP_AMT}=        Convert To Integer    ${DEP_AMT_TXT}

    Click Element    ${DEPOSIT_TAB}
    Sleep    ${WAIT}

    Wait Until Element Is Visible    ${AMOUNT_INPUT}    10
    Clear Element Text    ${AMOUNT_INPUT}
    Input Text           ${AMOUNT_INPUT}    ${DEP_AMT}
    Sleep    ${WAIT}

    Click Element    ${DEPOSIT_BTN}
    Wait Until Element Is Visible    ${MSG}    10
    ${msg1}=    Get Text    ${MSG}
    Should Contain    ${msg1}    Deposit Successful
    Sleep    ${WAIT}

    ${after_dep}=    Get Balance
    ${expected_dep}=    Evaluate    ${before} + ${DEP_AMT}
    Should Be Equal As Integers    ${after_dep}    ${expected_dep}
    Sleep    ${WAIT}

    ${WITH_AMT_TXT}=    Generate Random String    4    [NUMBERS]
    ${WITH_AMT}=        Convert To Integer    ${WITH_AMT_TXT}

    Click Element    ${WITHDRAWL_TAB}
    Sleep    ${WAIT}

    Wait Until Element Is Visible    ${AMOUNT_INPUT}    10
    Clear Element Text    ${AMOUNT_INPUT}
    Input Text           ${AMOUNT_INPUT}    ${WITH_AMT}
    Sleep    ${WAIT}

    Click Element    ${WITHDRAW_BTN}
    Wait Until Element Is Visible    ${MSG}    10
    ${msg2}=    Get Text    ${MSG}
    Should Contain    ${msg2}    Transaction successful
    Sleep    ${WAIT}

    ${after_wd}=    Get Balance
    ${expected_wd}=    Evaluate    ${after_dep} - ${WITH_AMT}
    Should Be Equal As Integers    ${after_wd}    ${expected_wd}
    Sleep    ${WAIT}

    Click Element    ${HOME_BTN}
    Sleep    ${WAIT}


*** Keywords ***
Open XYZ Bank
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.3s
    Wait Until Element Is Visible    ${BANK_MANAGER_BTN}    10

Get Balance
    ${txt}=    Get Text    ${BALANCE_VALUE}
    ${bal}=    Convert To Integer    ${txt}
    [Return]   ${bal}