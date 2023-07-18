import tkinter as tk
from tkinter import *

import sys

if __name__ == '__main__':

    # creating window
    root = Tk()
    filer_photo = r"C:\\Eyal\\Codes\\Random-projects-not-history-\\gui\\full screen+PhotoImage\\LPY.png"
    # Add image file
    bg = PhotoImage(file=filer_photo)
    # setting attribute
    root.attributes('-fullscreen', True)
    root.title("full")

    # Show image using label
    Label(root, image=bg,).place(x=50, y=50)
    # creating text label to display on window screen
    label = tk.Label(root, text="Hello Tkinter!",
                     font='arial 24 bold', bg='honeydew', fg="dark cyan")
    quit = tk.Button(root, text='quit', font='arial 24 bold', bg='honeydew', fg="dark cyan",
                     command=sys.exit)
    quit.pack()
    label.pack()
    root['bg'] = 'green'

    root.mainloop()
