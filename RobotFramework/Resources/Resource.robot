*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Login
    Log    Enter username
    Log    Enter password
    Log    Click on login button
    Log    User is on the home page


Launch Browser
        Log   Launching the browser
Close the Browser
        Log   Closing the browser

Launch Open_DB
        Log   Opening the DB
Launch Close_DB
        Log   Closing the DB