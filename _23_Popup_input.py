from tkinter import *
from tkinter import simpledialog


def get_me():
    s = simpledialog.askstring('Input string','Please enter your name')
    print(s)


root = Tk()
root.geometry('300x300')
B1 = Button(root, text='Click here to enter your name', command=get_me)
B1.pack()

root.mainloop()