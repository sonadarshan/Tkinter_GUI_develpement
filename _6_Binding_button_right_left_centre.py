from tkinter import *

root = Tk()
root.title("MY PROGRAM")


def right(event):
    print("U clicked Right")


def left(event):
    print("U clicked left")


def centre(event):
    print("U clicked c")


frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>", left)
frame.bind("<Button-2>", centre)
frame.bind("<Button-3>", right)
frame.pack()
root.mainloop()
