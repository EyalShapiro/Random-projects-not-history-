import random
import threading
import time

output = []
#שלטה על סדר רביצוע של תהליכים

def f(n):
    #time.sleep(0.5)
    output.append(n)


def main():
    threads = []
    list = []
    for i in range(random.randint(0, 10)):
        t = threading.Thread(target = f, args = (random.randint(0, 10),))
        threads.append(t)
        t.start()
    print(output)


if __name__ == '__main__':
    main()
