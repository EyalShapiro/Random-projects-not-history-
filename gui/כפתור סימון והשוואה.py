from tkinter import *
from tkinter.ttk import *

# creating root
root = Tk()
place_x = 20
place_y = 0


def main():
    global root, place_x, place_y
    while True:
        # label text
        Label(root, text='Select Programming language of your choice').place(
            x=place_x, y=place_y)

        # check buttons
        place_x += 5
        place_y += 25

        c = Checkbutton(root, text='C',
                        takefocus=0).place(x=place_x, y=place_y)
        place_y += 25
        cpp = Checkbutton(root, text='C++',
                          takefocus=0).place(x=place_x, y=place_y)
        place_y += 25
        cs = Checkbutton(root, text='C#',
                         takefocus=0).place(x=place_x, y=place_y)
        place_y += 25
        python = Checkbutton(root, text='Python',
                             takefocus=0).place(x=place_x, y=place_y)
        place_y += 25

        java = Checkbutton(root, text='Java',
                           takefocus=0).place(x=place_x, y=place_y)

        root.mainloop()


if __name__ == '__main__':
    main()
