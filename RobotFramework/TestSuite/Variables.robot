*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${name}       Jhon
${city}       jaipur
${address}    st.peter road
@{list1}      green    red    blue
@{list2}      apple    banana    grapes
&{creds}      username=admin    password=admin123

*** Test Cases ***
Print Variables And Lists
    Log    ${name}
    Log    ${city}
    Log    ${address}

    FOR    ${element}    IN    @{list1}
        Log    ${element}
    END

    FOR    ${element}    IN    @{list2}
        Log    ${element}
    END

    Log    ${creds}[username]
    Log    ${creds}[password]
    Log    ${list1}[0]
    Log    ${list2}[2]
