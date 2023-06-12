from gettext import install
from turtle import left
import pip
import pip._internal
from tkinter import *
import sys
import keyboard


# --------------------------------קבועים----------------------------------
_author_ = 'Eyal'
root = Tk()
root.geometry("250x200")
root.title("pip install")
text = Label(root, fg="gold4", height=2,
             width=16)
input_text = Text(root, fg='gold4', height=2,
                  width=24)
Output = Text(root, fg='gold4', height=4,
              width=24)
# ---------------------------------------------------------------------------


def press(num):
    "ctrl v  הדביקה"
    keyboard.send('ctrl+v')


def Pip_Install(name_package):
    """
    pip install a package python
    package[str]: שם של החבילה
    """
    help = 'pip install'
    if (help == name_package[0:len(help)]):  # בדיקה
        name_package = name_package[len(help):]
    if hasattr(pip, 'main'):
        pip.main(['install', name_package])
    else:
        pip._internal.main(['install', name_package])


def Take_input():
    name_package = input_text.get("2.4", "end-1c")
    print(name_package)
    Pip_Install(name_package)
    Output.insert(END, 'Install the Package')


def main():
    pr = Label(text="Enter name for package python\n ↓⇊↓ ")
    Display = Button(root, height=2, width=5, text="sand",
                     command=lambda: Take_input())
    v = Button(root, text='contrl v', width=6, command=lambda: press)
    pr.pack()
    input_text.pack()
    v.pack(side='right')

    Display.pack(side="left")
    Output.pack()
    quit = Button(root, text='quit', fg='gold4',
                  width=25, command=sys.exit)
    quit.pack()
    mainloop()


if __name__ == '__main__':
    main()
