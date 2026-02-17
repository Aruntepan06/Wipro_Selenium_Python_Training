#skip if difects aree there
#it the test cases are absolute
#window,mac -os depenc
#browser


import pytest

#definie Testcase1

def test_case1():
    print("Test Case1 pased")
@pytest.mark.skip
def test_case2():
    print("Test Case2 pased")
@pytest.mark.skip
def test_case3():
    print("Test Case3 pased")

def openbrowser():
    print("Open browser")
