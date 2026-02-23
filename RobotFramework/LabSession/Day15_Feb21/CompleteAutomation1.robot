*** Settings ***
Library    SeleniumLibrary
Library    String

*** Variables ***
${URL}        https://automationexercise.com/
${BROWSER}    chrome
${PASSWORD}   Arun@123
${PRODUCT}    Blue Top

*** Test Cases ***
#Test Case 1 - Register User
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#    Set Selenium Speed    0.2s
#
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#    Click Element    xpath=//a[contains(text(),'Signup / Login')]
#    Wait Until Element Is Visible    xpath=//h2[text()='New User Signup!']    15s
#
#    ${random}=    Generate Random String    6    [LETTERS]
#    ${email}=     Set Variable    arun${random}@gmail.com
#    Set Suite Variable    ${REGISTERED_EMAIL}    ${email}
#
#    Input Text    css:[data-qa="signup-name"]    Arun
#    Input Text    css:[data-qa="signup-email"]   ${REGISTERED_EMAIL}
#    Click Button  css:[data-qa="signup-button"]
#
#    Wait Until Element Is Visible    id=password    20s
#
#    Click Element    id=id_gender1
#    Input Text       id=password    ${PASSWORD}
#
#    Select From List By Value    id=days      10
#    Select From List By Value    id=months    5
#    Select From List By Value    id=years     2003
#
#    Click Element    id=newsletter
#    Click Element    id=optin
#
#    Scroll Element Into View    id=first_name
#    Input Text    id=first_name       Arun
#    Input Text    id=last_name        Kumar
#    Input Text    id=company          TestCompany
#    Input Text    id=address1         123 Street
#    Input Text    id=address2         Near Park
#    Select From List By Value     id=country    India
#
#    Input Text    id=state            Rajasthan
#    Input Text    id=city             Jaipur
#    Input Text    id=zipcode          500001
#    Input Text    id=mobile_number    9876543210
#
#    Scroll Element Into View    css:[data-qa="create-account"]
#    Click Button    css:[data-qa="create-account"]
#
#    Wait Until Page Contains Element    xpath=//b[normalize-space()='Account Created!']    20s
#    Click Element    css:[data-qa="continue-button"]
#
#    Wait Until Page Contains Element    xpath=//a[contains(text(),'Logged in as')]    20s
#    Close Browser


#Test Case 2 - Login With Correct Credentials
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#    Click Element    xpath=//a[contains(text(),'Signup / Login')]
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='Login to your account']    15s
#
#    Input Text    css:[data-qa="login-email"]       ${REGISTERED_EMAIL}
#    Input Text    css:[data-qa="login-password"]    ${PASSWORD}
#    Click Button  css:[data-qa="login-button"]
#
#    Wait Until Page Contains Element    xpath=//a[contains(text(),'Logged in as')]    20s
#    Close Browser
#
#
#Test Case 3 - Login With Incorrect Credentials
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#    Click Element    xpath=//a[contains(text(),'Signup / Login')]
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='Login to your account']    15s
#
#    Input Text    css:[data-qa="login-email"]       wrongemail@test.com
#    Input Text    css:[data-qa="login-password"]    wrongpass123
#    Click Button  css:[data-qa="login-button"]
#
#    Wait Until Page Contains Element    xpath=//p[normalize-space()='Your email or password is incorrect!']    20s
#
#    Close Browser
#
#Test Case 4 - Logout User
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#    Set Selenium Speed    0.2s
#
#    # Verify Home Page
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#
#    # Go to Login
#    Click Element    xpath=//a[contains(text(),'Signup / Login')]
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='Login to your account']    15s
#
#    # Login with correct credentials
#    Input Text    css:[data-qa="login-email"]       ${REGISTERED_EMAIL}
#    Input Text    css:[data-qa="login-password"]    ${PASSWORD}
#    Click Button  css:[data-qa="login-button"]
#
#    # Verify logged in
#    Wait Until Page Contains Element    xpath=//a[contains(text(),'Logged in as')]    20s
#
#    # Click Logout
#    Click Element    xpath=//a[contains(text(),'Logout')]
#
#    # Verify user navigated to login page
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='Login to your account']    20s
#
#    Close Browser

#Test Case 5 - Register User With Existing Email
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#    Set Selenium Speed    0.2s
#
#    # Verify Home Page
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#
#    # Click Signup / Login
#    Click Element    xpath=//a[contains(text(),'Signup / Login')]
#    Wait Until Element Is Visible    xpath=//h2[text()='New User Signup!']    15s
#
#    # Enter already registered email
#    Input Text    css:[data-qa="signup-name"]    Arun
#    Input Text    css:[data-qa="signup-email"]   ${REGISTERED_EMAIL}
#
#    Click Button  css:[data-qa="signup-button"]
#
#    # Verify error message
#    Wait Until Page Contains Element    xpath=//p[normalize-space()='Email Address already exist!']    20s
#
#    Close Browser

#Test Case 6 - Contact Us Form
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#    Set Selenium Speed    0.2s
#
#    # Verify Home Page
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#
#    # Click Contact Us
#    Click Element    xpath=//a[contains(text(),'Contact us')]
#
#    # Verify GET IN TOUCH visible
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='Get In Touch']    15s
#
#    # Fill Contact Form
#    Input Text    css:[data-qa="name"]      Arun
#    Input Text    css:[data-qa="email"]     arun@testmail.com
#    Input Text    css:[data-qa="subject"]   Testing Subject
#    Input Text    css:[data-qa="message"]   This is a test message for automation.
#
#    # Scroll to Upload Section
#    Scroll Element Into View    xpath=//input[@name='upload_file']
#
#    # Upload File (change path according to your system)
#    Choose File    xpath=//input[@name='upload_file']    /Users/arunkumartepan/Downloads/sampleFile.png
#    Sleep    3s
#      # Scroll to Submit button
#    Scroll Element Into View    css:[data-qa="submit-button"]
#
#    # Click Submit
#    Click Button    css:[data-qa="submit-button"]
#
#    # Handle Alert (Click OK)
#    Handle Alert    ACCEPT
#
#    # Verify Success Message
#    Wait Until Page Contains Element
#    ...    xpath=//div[contains(text(),'Success! Your details have been submitted successfully.')]    20s
#
#    # Scroll to Home button
#    Scroll Element Into View    xpath=//a[@class='btn btn-success']
#
#    # Click Home button
#    Click Element    xpath=//a[@class='btn btn-success']
#
#    # Verify navigated to Home page
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#
#    Close Browser

#Test Case 7 - Verify Test Cases Page
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#    Set Selenium Speed    0.2s
#
#    # Verify Home Page Visible
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    15s
#
#    # Click Test Cases
#    Click Element    xpath=//a[contains(text(),'Test Cases')]
#
#    # Verify navigation to Test Cases page
#    Wait Until Element Is Visible    xpath=//b[normalize-space()='Test Cases']    15s
#
#    Close Browser

#Test Case 8 - Verify All Products And Product Detail Page
#
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#    Set Selenium Speed    0.2s
#
#    # Home page visible
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    20s
#
#    # Click Products
#    Wait Until Element Is Visible    xpath=//a[contains(text(),'Products')]    20s
#    Click Element    xpath=//a[contains(text(),'Products')]
#
#    # Verify ALL PRODUCTS page
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='All Products']    20s
#    Location Should Contain    products
#
#    # Verify products list visible
#    Wait Until Element Is Visible    xpath=(//div[@class='product-image-wrapper'])[1]    20s
#
#    # Scroll and click View Product of first product
#    Scroll Element Into View    xpath=(//a[contains(@href,'/product_details') and contains(.,'View Product')])[1]
#    Click Element    xpath=(//a[contains(@href,'/product_details') and contains(.,'View Product')])[1]
#
#    # Verify navigated to product detail page
#    Wait Until Element Is Visible    xpath=//div[contains(@class,'product-information')]/h2    20s
#    Location Should Contain    product_details
#
#    # Verify product details
#    Page Should Contain Element    xpath=//div[contains(@class,'product-information')]/h2
#    Page Should Contain Element    xpath=//p[contains(.,'Category')]
#    Page Should Contain Element    xpath=//span[contains(.,'Rs.')]
#    Page Should Contain Element    xpath=//b[contains(.,'Availability')]
#    Page Should Contain Element    xpath=//b[contains(.,'Condition')]
#    Page Should Contain Element    xpath=//b[contains(.,'Brand')]
#
#    Close Browser


#Test Case 9 - Search Product
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    10s
#    Set Selenium Speed    0.2s
#
#    # Home page visible
#    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    20s
#
#    # Go to Products page
#    Click Element    xpath=//a[contains(text(),'Products')]
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='All Products']    20s
#    Location Should Contain    products
#
#    # Search product
#    Wait Until Element Is Visible    id=search_product    20s
#    Scroll Element Into View         id=search_product
#    Clear Element Text              id=search_product
#    Input Text                      id=search_product    ${PRODUCT}
#    Click Button                    id=submit_search
#
#    # Verify SEARCHED PRODUCTS heading
#    Wait Until Element Is Visible    xpath=//h2[normalize-space()='Searched Products']    20s
#
#    # Verify related products are visible (list/cards)
#    Wait Until Element Is Visible    xpath=//div[@class='features_items']//div[contains(@class,'product-image-wrapper')]    20s
#
#    # Verify each product name contains the searched word (case-insensitive)
#    @{names}=    Get WebElements    xpath=//div[@class='productinfo text-center']/p
#    FOR    ${el}    IN    @{names}
#        ${txt}=    Get Text    ${el}
#        Should Match Regexp    ${txt}    (?i).*${PRODUCT}.*
#    END
#
#    Close Browser

Test Case 10 - Verify Subscription In Home Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10s
    Set Selenium Speed    0.2s

    # Verify Home page visible
    Wait Until Element Is Visible    xpath=//img[@alt='Website for automation practice']    20s

    # Scroll down to footer
    Scroll Element Into View    xpath=//h2[normalize-space()='Subscription']

    # Verify SUBSCRIPTION text visible
    Page Should Contain Element    xpath=//h2[normalize-space()='Subscription']

    # Generate random email
    ${random}=    Generate Random String    5    [LETTERS]
    ${email}=     Set Variable    wipro${random}@gmail.com
    Sleep    4s

    # Enter email and click arrow button
    Input Text    id=susbscribe_email    ${email}
    Click Button  id=subscribe

    # Verify success message
    Wait Until Page Contains    You have been successfully subscribed!    20s

    Close Browser