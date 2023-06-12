import tkinter as tk
import sys
# creating window
window = tk.Tk()

# setting attribute
window.attributes('-fullscreen', True)
window.title("Geeks For Geeks")

# creating text label to display on window screen
label = tk.Label(window, text="Hello Tkinter!")
quit = tk.Button(window, text='quit', width=25, command=sys.exit)
quit.pack()
label.pack()

window.mainloop()
