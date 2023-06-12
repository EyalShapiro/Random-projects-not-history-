import pipes
import sys
import win32file
import win32pipe
from class_PipeServer import*


def main():
    t = PipeServer("CSServer")
    t.t()
    t.connect()
    t.write("Hello from Python :)")
    t.write("Closing now...")
    t.close()


if __name__ == '__main__':
    main()
