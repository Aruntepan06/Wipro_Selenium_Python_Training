import pytest

@pytest.fixture(params=["Chrome", "Firefox"])
def testbrowser(request):
    return request.param

def test_open_browser(testbrowser):
    print(f"Invoke {testbrowser} browser")
    assert testbrowser in ["Chrome", "Firefox"]


#selecting  even or odd
@pytest.fixture(params=[("even", 10), ("odd", 11)])
def number_data(request):
    return request.param

def test_select_number(number_data):
    number_type, num = number_data

    if number_type == "even":
        assert num % 2 == 0
        print(f"{num} is Even")
    else:
        assert num % 2 != 0
        print(f"{num} is Odd")