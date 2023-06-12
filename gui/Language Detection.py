# Import Module
from tkinter import *
from langdetect import *
from iso639 import languages

# Create Object
root = Tk()

# Set geometry
root.geometry("400x500")


def language_detection():
	text = T.get("1.0", 'end-1c')

	# Get Language code
	language_code = languages.get(alpha2=detect(text))
	l_d.config(text="Language Detected:- "+language_code.name)


# Text Box
T = Text(root)
T.pack()

# label
l_d = Label(root, text="Language Detected:- ")
l_d.pack(pady=10)

# Button
Button(root, text='Detect Language', command=language_detection).pack(pady=10)

# Execute Mainloop
root.mainloop()
