from tkinter import *

root = Tk()


def print_me():
    print(spin.get())


root.geometry('500x500')
root.title("Adding item to cart wala thing")
spin = Spinbox(from_=1, to=5)
spin.pack()

b1 = Button(root, text="Click", command=print_me)
b1.pack()

root.mainloop()
