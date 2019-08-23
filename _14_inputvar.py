from tkinter import *

root = Tk()


def gettext():
    print(s.get())


s = StringVar()
string_input = Entry(root, textvariable=s)
s.set("Its a predefined text")
b1 = Button(root, text='Click me', command=gettext)
b1.pack()
string_input.pack()

root.mainloop()