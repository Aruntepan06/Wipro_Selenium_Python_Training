import pytest

#definie Testcase1

def test_case1():
    print("Test Case1 pased")
@pytest.mark.sanity
def test_case2():
    print("Test Case2 pased")

@pytest.mark.sanity
@pytest.mark.regression
def test_case3():
    print("Test Case3 pased")

def openbrowser():
    print("Open browser")
