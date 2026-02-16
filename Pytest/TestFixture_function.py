
import pytest
# scope is run before and after every function



@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("user is logged out")


#Fixtures Class Level Fixture Usage

@pytest.mark.usefixtures("openbrowser", "closebrowser")
class TestLogin:

    def test_login(self):
        print("enter the username")
        print("enter the password")
        print("click on the login button")

    def test_logout(self):
        print("user is logged out")

#Fixtures Module Level Fixture Usage

pytestmark = pytest.mark.usefixtures("openbrowser", "closebrowser")

def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")

def test_logout():
    print("user is logged out")