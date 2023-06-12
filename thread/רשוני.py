import random
import threading
import time

output = []
#שלטה על סדר רביצוע של תהליכים

def f(num):
    count = 0
    time.sleep(1)
    for i in range(1000):
        if num % i == 0:
            count += 1
    if count > 2:
        output.append(num)
    else:
        pass

def main():
    threads = []
    list = []
    for i in range(4):
        for i in range(250):
            t = threading.Thread(target = f, args = (i,))
            threads.append(t)
            t.start()
        print(output)


if __name__ == '__main__':
    main()
