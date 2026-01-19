import threading
import time

def print_lowercase():
    for c in range(ord('a'), ord('z') + 1):
        print(chr(c), end=' ')
        time.sleep(0.05)

def print_uppercase():
    for c in range(ord('A'), ord('Z') + 1):
        print(chr(c), end=' ')
        time.sleep(0.05)

t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)

t1.start()
t2.start()

t1.join()
t2.join()
