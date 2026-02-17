import pytest

#used inside the class
#it will run for every class definition, it will run starting and ending of the class

class TestDatabase:


    def setup_class(cls):
        print("Open DB connection")


    def teardown_class(cls):
        print("Close DB connection")

    def test_read(self):
        print("Reading the db")

    def test_write(self):
        print("Writing to the db")

    def test_update(self):
        print("Updating the db")


class TestClass:
    def setup_class(cls):
        print("Open web browser")

    def teardown_class(cls):
        print("Close web browser")

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