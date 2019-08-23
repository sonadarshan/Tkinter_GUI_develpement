from tkinter import *

root = Tk()
root.title('LabelFrame')
root.geometry('300x300')
labelframe = LabelFrame(root, text='Labelframe', padx=2, pady=2)
entry = Entry(labelframe)
entry.pack()
labelframe.pack()
root.mainloop()