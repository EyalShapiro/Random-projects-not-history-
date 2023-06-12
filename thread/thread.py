import random
import threading

"""
יצירת תהליך המזמן פונקציה המדפיסה f1 מאה פעמים. (פונקציה אחת, תהליך אחד)
יצירת תהליך המזמן פונקציה המדפיסה f2 מאה פעמים. (פונקציה אחת, תהליך אחד)
יצירת 2 תהליכים המזמנים פונקציה המדפיסה f1 או f2 לפי מספר התהליך (1 או 2). (פונקציה אחת, 2 תהליכים)
יצירת 5 תהליכים בלולאת for המזמנים פונקציה המדפיסה את המספר הסידורי של התהליך. (פונקציה אחת, 5 תהליכים בלולאה)
"""


def f1():  # 100 מדפיס f1
    for i in range(100):
        print('f1')


def f2():  # 100 מדפיס f2
    for i in range(100):
        print('f2')


def f3(f):
    for i in range(100):
        print(f)


def f4(f):
    print(f)


def main():
    # ex1-------------------------------------------
    # t1 = threading.Thread(target = f1)
    # t2 = threading.Thread(target = f2)
    # t1.start()
    # t2.start()
    # ex2-------------------------------------------
    # t1 = threading.Thread(target = f3,args = ['f1'])
    # t2 = threading.Thread(target = f3,args = ['f2'])
    # t1.start()
    # t2.start()
    list = []
    for i in range(1, 6):
        list.append(i)
    print(list)
    for i in range(len(list)):
        r = random.choice(list)
        list.remove(r)
        t = threading.Thread(target=f4, args=[r])
        t.start()


if __name__ == '__main__':
    main()
