import threading
import time

def task():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

t = threading.Thread(target=task)
t.start()
t.join()

print("Thread terminated")