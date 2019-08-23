from tkinter import *


def open_me():
    top = Toplevel()
    top.title("I am a new window")
    top.geometry('300x300')
    b1 = Button(top, text='Close', command=top.destroy)
    # Top.quit to colse the complete application and destroy is to just close the current window
    b1.pack()


root = Tk()
root.title('Main Window')
root.geometry('600x600')
b2 = Button(root, text='Click', command=open_me)
b2.pack()

root.mainloop()
