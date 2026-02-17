import pytest

@pytest.mark.usefixture("sessiosetup")

def test_one():
    print("testcase1")

def test_two():
    print("testcase2")
