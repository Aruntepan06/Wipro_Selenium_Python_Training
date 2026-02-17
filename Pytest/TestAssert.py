# basic assertion

#import pytest_check as check


# hard assertions - this will stop the execution of the test cases / test suite
# soft assertions will continue to run even if the assertions fails


# basic assertion
def test_add():
    result = 2 + 3
    assert result == 5


# checking true or false
def test_boolean():
    assert True
    assert not False


def test_none():
    value = None
    assert value is None


# list assertion
def test_list():
    fruitts = ["apple", "banana", "orabge"]
    assert "banana" in fruitts


# Dict assertion
def test_dict():
    creds_ = {"username": "admin", "password": "admin123"}
    assert creds_["password"] == "admin123"


# comparing lists
def test_comparelist():
    assert [1,2,3] == [1,2,3]

# assertion with custom message

def test_custommsg():
    result = 10
    assert result == 10, "Result should be 5"

 #
 # #soft Assertion
 # def test_multiple():
 #    check.equal(1,2)
 #    check.equal(2,3)

