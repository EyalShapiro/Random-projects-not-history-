from tkinter import *
from tkinter import filedialog
import sys
_author_ = 'Eyal'


def Open_File():
    """ נותן ליבחור הקבצה"""

    return filedialog.askopenfilename()


def Name_File():
    """שומרת אמיקום של הקובץ"""
    name = Open_File()
    return name


if __name__ == '__main__':
    while True:
        root = Tk()
        openfile = Button(root, text="Open", width=20, command=Name_File)
        openfile.grid(column=5, row=5)

        quit = Button(root, text="QUIT", fg="green", command=root.destroy)
        quit.grid(column=5, row=6)
        print(Name_File())
        root.mainloop()
        r = Tk()
        sure = Label(text="You're sure you want to close")

        yes = Button(r, text="Yes", command=sys.exit)
        no = Button(r, text="No", command=root.destroy())
        sure.pack()
        yes.pack()
        no.pack()
        r.mainloop()
