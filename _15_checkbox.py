from tkinter import *
from tkinter import messagebox

root = Tk()


def getthevalue():
    print(i.get())
    if i.get() == 1 or i.get()=='checked':
        messagebox.showinfo("Good", "U accepted my challenge")

# We can even give custom value for checked and unchecked
#i = StringVar()
#check = Checkbutton(root, text="Click me if you can", variable=i, offvalue='unchecked', onvalue='checked')
i = IntVar()
check = Checkbutton(root, text="Click me if you can", variable=i)
check.pack()
b1 = Button(root, text='Click me', command=getthevalue)
b1.pack()

root.mainloop()