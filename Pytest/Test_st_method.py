import pytest

# used inside the class
# runs before and after the test methods  inside the class
#incase of inheritance it will work for set up and teardonw

class TestDatabase:
    def setup_mehtod(method):
        print("Opening the Mehtod")
    def teardown_mehtod(method):
        print("Closing the Mehtod")
    def test_read(self):
        print("Reading the browser")

    def test_write(self):
        print("Writing to the browser")

    def test_update(self):
        print("Updating the browser")

