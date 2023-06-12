import threading
import time


s = threading.Semaphore(3)
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


def main():
    for i in range(1, 11):
        threading.Thread(target=f, args = (i,)).start()


if __name__ == '__main__':
    main()
