
import pytest
@pytest.fixture
def simple_data():
    return 45


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current browser:", request.param)
    return request.param

@pytest.fixture()
def api_url():
    return  "https://api.example.com"

@pytest.fixture(scope = 'function')
def openbrowser():
    # precondition
    print("open the browser")

@pytest.fixture(scope = 'function')
def closebrowser():
     # post condition
    print("closing the browser")