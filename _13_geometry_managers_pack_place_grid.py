from tkinter import *

root = Tk()
root.title('Geometry manager')
root.geometry('500x500')
# PACK
# label1 = Label(root,text='I am biegn packed')
# label1.pack(side=TOP)

# Grid
# label2 = Label(root,text='I am in a grid')
# label2.grid(row=2,column=2)

#Place
label1 = Label(root, text="I am bieng placed")
label1.place(x=200, y=200)

root.mainloop()

