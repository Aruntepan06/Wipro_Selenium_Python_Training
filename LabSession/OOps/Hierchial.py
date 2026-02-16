#hierchial.py
class Employee:
    def login(self):
        print("Employee loged in")

class Developer(Employee):
    def write_code(self):
        print("writing code")


class Tester(Employee):
    def test_app(self):
        print("Test the application")


dev=Developer()
test=Tester()

dev.login()
dev.write_code()
test.login()
test.test_app()