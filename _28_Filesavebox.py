from tkinter import *
from tkinter import filedialog


def save_file():
    result = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if result is None:
        return
    result.write('Hello Hai how are you')
    result.close()


root = Tk()
root.title("Save ur file")
root.geometry('400x400')
b1 = Button(root, text='Click', command=save_file)
b1.pack()

root.mainloop()