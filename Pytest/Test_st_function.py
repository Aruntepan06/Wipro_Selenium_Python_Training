# function level set up and tear down
# these run before and after each test function
import pytest
#opent the browser
def setup_function(function):
    print("opening the browser")

def tearingdown_function(function):
    print("opening the browser")

@pytest.mark.sanity
def test_case1():
    print("Test Case1 pased")
@pytest.mark.regression
def test_case2():
    print("Test Case2 pased")

def test_case3():
    print("Test Case3 pased")
