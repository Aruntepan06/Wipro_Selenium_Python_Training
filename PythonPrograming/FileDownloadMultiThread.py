import threading
import time

def download_file(file_name):
    print(f"Downloading the file: {file_name}")
    time.sleep(2)
    print(f"{file_name} downloaded")



files = ["file1.txt", "file2.txt", "file3.txt"]


threads = [threading.Thread(target=download_file, args=(file_name,)) for file_name in files]


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()
