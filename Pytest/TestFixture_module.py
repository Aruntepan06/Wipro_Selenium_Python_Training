import pytest

#Fixtures Module Level Fixture Usage


pytestmark = pytest.mark.usefixtures("setupapi")

def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")

def test_logout():
    print("user is logged out")