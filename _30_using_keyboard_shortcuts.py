from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Use the shortcut Ctrl+F')
root.geometry('450x450')

def opensg(event=''):
    messagebox.showinfo('Hai buddy', 'U pressed Cntrl+F')


root.bind('<Control-f>', opensg)
b1 = Button(root, text='click if u dont have keyboard', command=opensg)
b1.pack()

root.mainloop()



