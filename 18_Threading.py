import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(3):
            print(f"{self.name} is running")
            time.sleep(1)


def print_numbers():
    for i in range(3):
        print("Number:", i)
        time.sleep(1)


# Thread using class
thread1 = MyThread("Thread-1")

# Thread using function
thread2 = threading.Thread(target=print_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main thread finished")
