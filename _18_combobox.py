from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Combo Box Example")
root.geometry('600x600+100+100')


def print_me():
    print(combo.get())


v = ['C++', 'java', 'C', 'C#', 'Python', 'Css', 'Javascript']
combo = Combobox(root, values=v, width=15)
combo.set('Select')
combo.pack()
B1 = Button(root, text='Print me', command=print_me)
B1.pack()

root.mainloop()