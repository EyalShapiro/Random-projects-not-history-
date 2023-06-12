# Importing tkinter module
from tkinter import *
# from tkinter.ttk import *

# creating Tk window
master = Tk()


def main():
    # creating a Fra, e which can expand according
    # to the size of the window
    pane = Frame(master)
    pane.pack(fill=BOTH, expand=True)

    # button widgets which can also expand and fill
    # in the parent widget entirely
    # Button 1
    b1 = Button(pane, text="Click me !",
                background="green", fg="white")

    # Button 2
    b2 = Button(pane, text="Click me too",
                background="blue", fg="white")

    # Button 3
    b3 = Button(pane, text="quit",
                background="red", fg="white", command=pane.quit)
    b1.pack(side=TOP, expand=True, fill=BOTH)
    b2.pack(side=TOP, expand=True, fill=BOTH)
    b3.pack(side=TOP, expand=True, fill=BOTH)

    # Execute Tkinter
    master.mainloop()


if __name__ == '__main__':
    main()
