# Destructors - When we want to destroy the object
# post conditions - closing of the browser, db connection closing, releasing of certain resources
# clean up operations
# for proper memory usage destructors should be used
# when db connection has to be closed -
# free the memory (garbage collection) which is automatically called
# Destructor runs when program ends or object is garbage-collected.

class Desct:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Closing the db connection")

a = Desct()
print("End of the program")

# desct in file handling
del a

# desct in file handling

class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print("File is opened")

    def readfile(self, filename):
        print("Reading the file")

f=FileHandler("test.txt")
print("End of the program")
del f