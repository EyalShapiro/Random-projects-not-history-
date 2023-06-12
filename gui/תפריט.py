import tkinter as tk
from tkinter import *

LARGE_FONT = ("Verdana", 12, 'underline', 'bold')
SMALL_FONT = ('Helvetica', 10, 'underline')

# MTC = Macro Time Controller


class MTC(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Macro Slider - Time Lapse - Controller")

        container = tk.Frame(self, borderwidth=5, relief="sunken")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page3):
            frame = F(container, self,)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="news")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=30, padx=30)

        button = tk.Button(self, text="Steppermotor Test", font=SMALL_FONT,
                           command=lambda: controller.show_frame(Page1))
        button.place(x=50, y=125, height=80, width=110)

        button2 = tk.Button(self, text="Macro Stacking", font=SMALL_FONT,
                            command=lambda: controller.show_frame(Page2))
        button2.place(x=250, y=125, height=80, width=110)

        button3 = tk.Button(self, text="Time Lapse", font=SMALL_FONT,
                            command=lambda: controller.show_frame(Page3))
        button3.place(x=450, y=125, height=80, width=110)

        button4 = tk.Button(self, text="In Development", font=SMALL_FONT,
                            command=lambda: controller.show_frame(Page4))
        button4.place(x=650, y=125, height=80, width=110)

        button5 = tk.Button(self, text="Quit", font=SMALL_FONT,
                            command=self.quit)
        button5.place(x=350, y=300, height=80, width=110)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Time Lapse!!!", font=LARGE_FONT)
        label.pack(pady=30, padx=30)

        def on_entry_click1(event):
            """function that gets called whenever entry is clicked"""
            if e1.get() == 'Enter settings 1...':
                e1.delete(0, "end")  # delete all the text in the entry
                e1.insert(0, '')  # Insert blank for user input
                e1.config(fg='black')

        def on_entry_click2(event):
            """function that gets called whenever entry is clicked"""
            if e2.get() == 'Enter settings 2...':
                e2.delete(0, "end")  # delete all the text in the entry
                e2.insert(0, '')  # Insert blank for user input
                e2.config(fg='black')

        def on_entry_click3(event):
            """function that gets called whenever entry is clicked"""
            if e3.get() == 'Enter settings 3...':
                e3.delete(0, "end")  # delete all the text in the entry
                e3.insert(0, '')  # Insert blank for user input
                e3.config(fg='black')

        def on_entry_click4(event):
            """function that gets called whenever entry is clicked"""
            if e4.get() == 'Enter settings 4...':
                e4.delete(0, "end")  # delete all the text in the entry
                e4.insert(0, '')  # Insert blank for user input
                e4.config(fg='black')

        def set_text(text):
            e1.insert(END, text)
            return

        def set_text(text):
            e2.insert(END, text)
            return

        def set_text(text):
            e3.insert(END, text)
            return

        def set_text(text):
            e4.insert(END, text)
            return

        def toggle():
            if t_btn.config('text')[-1] == 'Forward':
                t_btn.config(text='Reverse')
            else:
                t_btn.config(text='Forward')

        button1 = Button(self, text="Back to Main Menu",
                         command=lambda: controller.show_frame(StartPage))
        button1.pack(padx=50, pady=15)

        tk.Radiobutton(self, text="Full Step", indicatoron=0,
                       width=6, padx=20, value=1, variable=1).place(x=20, y=150)

        tk.Radiobutton(self, text="Half Step", indicatoron=0, width=6,
                       padx=20, value=2, variable=1).place(x=110, y=150)

        tk.Radiobutton(self, text="Quarter Step", indicatoron=0,
                       width=6, padx=20, value=3, variable=1).place(x=200, y=150)

        tk.Radiobutton(self, text="Either Step", indicatoron=0,
                       width=6, padx=20, value=4, variable=1).place(x=290, y=150)

        tk.Radiobutton(self, text="Sixteenth Step", indicatoron=0,
                       width=6, padx=20, value=5, variable=1).place(x=380, y=150)

        t_btn = Button(self, text="Forward", width=12, command=toggle)
        t_btn.place(x=250, y=350)

        tk.button = Button(self, text='Move', width=12).place(x=350, y=350)

        e1 = Entry(self, bd=1, width=10, justify=RIGHT)
        e1.insert(0, 'Enter settings 1...')
        e1.bind('<FocusIn>', on_entry_click1)
        e1.config(fg='red')
        e1.place(x=25, y=200)

        label1 = tk.Label(self, text="Input 1")
        label1.place(x=100, y=200)

        e2 = Entry(self, bd=1, width=10, justify=RIGHT)
        e2.insert(0, 'Enter settings 2...')
        e2.bind('<FocusIn>', on_entry_click2)
        e2.config(fg='red')
        e2.place(x=25, y=225)

        label2 = tk.Label(self, text="Input 2")
        label2.place(x=100, y=225)

        e3 = Entry(self, bd=1, width=10, justify=RIGHT)
        e3.insert(0, 'Enter settings 3...')
        e3.bind('<FocusIn>', on_entry_click3)
        e3.config(fg='red')
        e3.place(x=25, y=250)

        label3 = tk.Label(self, text="Input 3")
        label3.place(x=100, y=250)

        e4 = Entry(self, bd=1, width=10, justify=RIGHT)
        e4.insert(0, 'Enter settings 4...')
        e4.bind('<FocusIn>', on_entry_click4)
        e4.config(fg='red')
        e4.place(x=25, y=275)

        label4 = tk.Label(self, text="Input 4")
        label4.place(x=100, y=275)

# Numeric Keypad

        sev = tk.Button(self, bd=3, text="7", command=lambda: set_text("7"))
        sev.place(x=600, y=150, width=50, height=50)
        eig = tk.Button(self, bd=3, text="8", command=lambda: set_text("8"))
        eig.place(x=650, y=150, width=50, height=50)
        nin = tk.Button(self, bd=3, text="9", command=lambda: set_text("9"))
        nin.place(x=700, y=150, width=50, height=50)

        fou = tk.Button(self, bd=3, text="4", command=lambda: set_text("4"))
        fou.place(x=600, y=200, width=50, height=50)
        fiv = tk.Button(self, bd=3, text="5", command=lambda: set_text("5"))
        fiv.place(x=650, y=200, width=50, height=50)
        six = tk.Button(self, bd=3, text="6", command=lambda: set_text("6"))
        six.place(x=700, y=200, width=50, height=50)

        one = tk.Button(self, bd=3, text="1", command=lambda: set_text("1"))
        one.place(x=600, y=250, width=50, height=50)
        two = tk.Button(self, bd=3, text="2", command=lambda: set_text("2"))
        two.place(x=650, y=250, width=50, height=50)
        thr = tk.Button(self, bd=3, text="3", command=lambda: set_text("3"))
        thr.place(x=700, y=250, width=50, height=50)

        dot = tk.Button(self, bd=3, text=".", command=lambda: set_text("."))
        dot.place(x=600, y=300, width=50, height=50)
        zer = tk.Button(self, bd=3, text="0", command=lambda: set_text("0"))
        zer.place(x=650, y=300, width=50, height=50)
        bck = tk.Button(self, bd=3, text="Del")
        bck.place(x=700, y=300, width=50, height=50)


app = MTC()
app.geometry("800x480+200+0")
app.mainloop()
