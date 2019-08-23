from tkinter import *

root = Tk()

label1 = Label(root, text='Hello', bg='red')
# To display the label full width matched to that of parent
label1.pack(fill=X)
label2 = Label(root, text='hai', bg='white')
label2.pack(side=LEFT, fill=Y)
label3 = Label(root, text='Ola', bg='yellow')
label3.pack(side=RIGHT, fill=Y)
root.mainloop()