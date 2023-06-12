# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()


def main():
    pass


if __name__ == '__main__':
    main()

    while True:
        quit = Button(root, text="quit", command=root.destroy,
                      compound=print("Quit"))
        btn1 = Button(root, text="Button ", command=quit.destroy,
                      compound=print("Button"))
        btn1.pack(pady=10)
        quit.pack(pady=10)
        # infinite loop
        mainloop()
