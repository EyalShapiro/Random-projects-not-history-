from tkinter import *

_author_ = 'Eyal'

root = Tk()
root.geometry("300x300")
root.title(" Q&A ")
input_text = Text(root, height=10,
                  width=25, bg="light yellow")
Output = Text(root, height=5,
              width=25,
              bg="light cyan")


def Take_input():
    text = input_text.get("1.0", "end-1c")
    print(text)
    if (input_text == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")


def main():
    pr = Label(text="What is 24 * 5 ? ")
    Display = Button(root, height=2, width=20, text="Show",
                     command=lambda: Take_input())
    pr.pack()
    input_text.pack()
    Display.pack()
    Output.pack()

    mainloop()


if __name__ == '__main__':
    main()
