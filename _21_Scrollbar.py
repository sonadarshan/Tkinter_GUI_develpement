from tkinter import *

root = Tk()
frame = Frame(root)
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)
listbox = Listbox(frame, yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
for i in range(100):
    listbox.insert(i, str(i))
listbox.pack(side=TOP)
frame.pack()
root.mainloop()