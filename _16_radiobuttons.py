from tkinter import *
from tkinter import messagebox

root = Tk()


def getthevalue():
    print(i.get())
    if i.get() == 1 :
        messagebox.showinfo("Good", "Male")
    elif i.get() == 2:
        messagebox.showinfo("Oh..", "U are female")


i = IntVar()
m = Radiobutton(root, text="Male", variable=i, value=1)
f = Radiobutton(root, text="Female", variable=i, value=2)
m.pack()
f.pack()
b1 = Button(root, text='Click me', command=getthevalue)
b1.pack()

root.mainloop()