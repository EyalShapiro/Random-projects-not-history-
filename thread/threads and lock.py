import threading
import time

lock = threading.Lock()  # מנעול


def f1():
    for i in range(100):
        lock.acquire()
        print('f1')
        lock.release()


def f2():
    for i in range(100):
        lock.acquire()
        print('f2')
        lock.release()


def f3(n):
    for i in range(100):
        print('f' + str(n))


t1 = threading.Thread(target=f1)  # הגדרה של תהליך
t1.start()  # הפעלה של תהליך
t2 = threading.Thread(target=f2)  # הגדרה של תהליך
t2.start()  # הפעלה של תהליך
t3 = threading.Thread(target=f3, args=(1,))  # הגדרה של תהליך עם פרמטר
t3.start()  # הפעלה של תהליך
t4 = threading.Thread(target=f3, args=(2,))  # הגדרה של תהליך עם פרמטר
t4.start()  # הפעלה של תהליך

outputs = []


def f(n):
    time.sleep(0.1)
    # print(n)
    outputs.append(n)


threads = []
for i in range(5):
    t = threading.Thread(target=f, args=(i,))
    threads.append(t)
    t.start()


for i in range(5):
    threads[i].join()
    print(outputs[i])
