import pytest
import sys
# @pytest.mark.xfail(reason="Known bug in the third-party library")
# def test_function_with_bug():
#     assert (1 + 1) == 3  # This assertion will fail as expected
# def test_case1():
#     print("Test Case1 pased")
#
# def test_case2():
#     print("Test Case2 pased")
#
# def test_case3():
#     print("Test Case3 pased")

# xfail with a condition
@pytest.mark.xfail(sys.platform == "win32", reason="Bug on windows")
def test():
    print("test on windows")


# this xfail will fail only on windows


# strict=True  XFAIL  failed  Fails the test suite
@pytest.mark.xfail(strict=True, reason="Bug #1234 is not fixed yet")
def test_function():
    assert True


# the testcase should fail mandatorily