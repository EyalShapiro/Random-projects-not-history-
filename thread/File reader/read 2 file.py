from os import popen
import threading
import time
import socket
from Create_File import *
# =====================
out_file = Create_File()
lock_all = threading.Semaphore(3)
lock = threading.Lock()
# =====================


def Read_File(filename):
    """
    הפעולה מקבלת שם של קובצה 
    הפעולה מחזרה רשמה של המילים שרשומים 
    """
    list_file = []
    with open(filename) as all_file:
        readfile = all_file.readlines()
        list_file = readfile.split(' ')
        return list_file


# def File_Out(filename1):
#     """
#     הפעולה מקבלת שם של קובצה
#     ומשלבת בנים בזרת
#     Class : Create_File
#     """
#     global cfile
#     sline = Read_File(filename1)
#     for i in sline:
#         cfile.Write(i)
#     cfile.Closed()

def f(list_file):
    pass
    # lock_all = threading.Semaphore(3)
    # lock = threading.Lock()
    # actives = []
    # lock_all.acquire()
    # lock.acquire()
    # actives.append(n)
    # print(actives)
    # lock.release()
    # time.sleep(3)
    # lock.acquire()
    # actives.remove(n)
    # print(actives)
    # lock.release()
    # lock_all.release()


def main():
    global out_file
    global lock_all
    global lock
    # file1 = Read_File("f1.txt")
    # print(file1)
    # file2 = Read_File("f2.txt")
    thread_file1 = threading.Thread(target=Read_File, args="f2.txt").start()
    thread_file2 = threading.Thread(target=Read_File, args="f2.txt").start()
    for i in len():
        lock_all.acquire()
        lock.acquire()
        out_file.Write()

    print(thread_file1)


if __name__ == '__main__':
    main()
