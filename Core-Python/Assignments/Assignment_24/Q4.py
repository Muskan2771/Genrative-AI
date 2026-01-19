import threading
import time
import random

buffer = []
buffer_size = 5
condition = threading.Condition()

def producer(pid):
    global buffer
    for i in range(5):
        item = random.randint(1, 100)
        with condition:
            while len(buffer) == buffer_size:
                condition.wait()
            buffer.append(item)
            print(f"Producer {pid} produced {item}")
            condition.notify()
        time.sleep(1)

def consumer(cid):
    global buffer
    for i in range(5):
        with condition:
            while len(buffer) == 0:
                condition.wait()
            item = buffer.pop(0)
            print(f"Consumer {cid} consumed {item}")
            condition.notify()
        time.sleep(1)

producers = [
    threading.Thread(target=producer, args=(1,)),
    threading.Thread(target=producer, args=(2,))
]

consumers = [
    threading.Thread(target=consumer, args=(1,)),
    threading.Thread(target=consumer, args=(2,))
]

for p in producers:
    p.start()

for c in consumers:
    c.start()

for p in producers:
    p.join()

for c in consumers:
    c.join()
