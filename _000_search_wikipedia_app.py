from tkinter import *
import wikipedia
from tkinter.font import Font


def print_me():
    user_input = str(e1.get())
    try:
        results = wikipedia.summary(user_input)
    except wikipedia.exceptions.PageError as msg:
        results = str(msg)
    textbox.delete(1.0, END)
    textbox.insert(INSERT, results)


root = Tk()
root.geometry('600x600')
my_font = Font(family='Times New Roman', size=16, weight='bold')
label = Label(root, text='Search Wiki', font=my_font)
label.pack()
e1 = Entry(root)
e1.pack()
B1 = Button(root, text='Click', command=print_me)
B1.pack()
frame = Frame(root)
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)
textbox = Text(frame, width=100, height=30, wrap=WORD, padx=10, pady=10, bd=5, selectbackground='blue', yscrollcommand=scroll.set)
scroll.config(command=textbox.yview)
textbox.pack()
frame.pack()


root.mainloop()