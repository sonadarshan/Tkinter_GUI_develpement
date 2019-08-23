from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('Changing background color')
root.geometry('500x500')


def change_color():
    clr = colorchooser.askcolor(title='Select color')
    # It returns a tuple with RGB values at 0th index and color hexvalue at 1st index
    root.configure(background=clr[1])


b1 = Button(root, text='Chnage background', command=change_color)
b1.pack()

root.mainloop()