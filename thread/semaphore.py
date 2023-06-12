import threading
import time

s = threading.Semaphore(4)
l = threading.Lock()
actives = []


def f(n):
    s.acquire()
    l.acquire()
    actives.append(n)
    print(actives)
    l.release()
    time.sleep(3)
    l.acquire()
    actives.remove(n)
    print(actives)
    l.release()
    s.release()


def Start_Thread(number):
    for i in range(1, number):
        threading.Thread(target=f, args=(i,)).start()


def main():
    Start_Thread(15)


if __name__ == '__main__':
    main()
