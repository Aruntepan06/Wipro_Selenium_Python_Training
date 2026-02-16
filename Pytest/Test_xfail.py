import pytest

@pytest.mark.xfail(reason="Known bug in the third-party library")
def test_function_with_bug():
    assert (1 + 1) == 3  # This assertion will fail as expected
def test_case1():
    print("Test Case1 pased")

def test_case2():
    print("Test Case2 pased")

def test_case3():
    print("Test Case3 pased")
