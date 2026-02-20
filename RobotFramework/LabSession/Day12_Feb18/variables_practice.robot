*** Settings ***
Library    Collections

*** Variables ***
${NAME}        Arun
${CITY}        Jaipur
@{FRUITS}      Apple    Banana    Mango
&{USER}        name=Arun    age=22

*** Test Cases ***
Variables Practice

    # 1. Print scalar variable
    Log    ${NAME}

    # 2. Assign two numbers and print sum
    ${num1}=    Set Variable    10
    ${num2}=    Set Variable    20
    ${sum}=     Evaluate    ${num1} + ${num2}
    Log    ${sum}

    # 3. Use CITY inside sentence
    Log    I live in ${CITY}

    # 4. Reassign variable value
    ${NAME}=    Set Variable    John
    Log    Updated name is ${NAME}

    # 5. Print first item of list
    Log    ${FRUITS}[0]

    # 6. Loop through list
    FOR    ${fruit}    IN    @{FRUITS}
        Log    ${fruit}
    END

    # 7. Find length of list
    ${length}=    Get Length    ${FRUITS}
    Log    ${length}

    # 8. Print dictionary key value
    Log    ${USER}[name]

    # 9. Add new key-value to dictionary
    Set To Dictionary    ${USER}    city=Jaipur
    Log    ${USER}[city]

    # 10. Loop dictionary key and value
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} = ${value}
    END
