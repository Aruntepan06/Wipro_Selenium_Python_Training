def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def vanillacake():
    print("I am the vanilla  cake")

@make_pretty
def staraberrcake():
    print("I am the starberry cake")

vanillacake()
staraberrcake()