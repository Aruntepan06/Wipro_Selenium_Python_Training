import pytest
from Test_SimpleFixture import  api_url
def test_case1():
    print("Test Case1 pased")

def test_case2():
    print("Test Case2 pased")

def test_case3():
    print("Test Case3 pased")

def test_case4():
    print("Test Case4 pased")

def test_case5():
    print("Test Case5 pased")

def test_login():
    print("Test login")

def test_api_url(api_url):
    assert "https://api.example.com" in api_url

