import threading


def number():
    for i in range(10):
        print("Number: ",i)

def letter():
    for k in "ABCDEFG":
        print("Letter: ",k)


t1=threading.Thread(target=number)
t2=threading.Thread(target=letter)
t1.start()
t2.start()
t1.join()
t2.join()

