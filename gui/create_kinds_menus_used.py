'''
Menu: It is used to create all kinds of menus used by the application.
The general syntax is:
There are number of options which are used to change the format of this widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.
'''
from tkinter import *
from tkinter import filedialog
root = Tk()


def Open_File():
    """ נותן ליבחור הקבצה"""
    return filedialog.askopenfilename()


def Name_File():
    """שומרת אמיקום של הקובץ"""
    name = Open_File()
    return name


def main():
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...', command=Name_File)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
    mainloop()


if __name__ == '__main__':
    main()
