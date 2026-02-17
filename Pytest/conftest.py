
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

@pytest.fixture(scope="class")
#when we use yield automatice tear down happen
def dbconnection():
    # precondition
    print("open the db connection")   # code before the yield - set up
    yield
    print("closing the db conenction")  # code after the yield - teardown

@pytest.fixture
def setup():
    print("Setup")
    return "data"

@pytest.fixture(scope="module")
#when we use yield automatice tear down happen
def setupapi():
    # precondition
    print("authorise the api")   # code before the yield - set up
    yield
    print("Unauthorise the api")  # code after the yield - teardown

@pytest.fixture(scope = "session")
def sessionsetup():
    print("Tests started on QA environment ") # setup
    yield
    print("Tests finished on QA environment") # tear down


#fixture Dependency

@pytest.fixture()
def fixture_a():
    return "Data from A"

@pytest.fixture()
def fixture_b(fixture_a): # calling another fixture
    return f"{fixture_a} + Data from B"