from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('600x600+100+100')
root.title('Textbox')

#1.0 indicated 1st line 0th index
def print_me():
    print(textbox.get(1.0,END))


def print_selected():
    print(textbox.selection_get())
    print(textbox.search(textbox.selection_get(), 1.0, stopindex=END))


def clear():
    textbox.delete(1.0,END)


fonts = Font(family='Roman')
# wrap - complete word comes in a line
# padx and pady -margin
# bd is borderwidth by default it is 2
# text selection color is set through the selectbackground
textbox = Text(root, width=20, height=10, wrap=WORD, padx=10, pady=10, bd=5, selectbackground='blue', font=fonts, background='black')
textbox.pack()
# To display the predefined text
textbox.insert(INSERT, "Hello I am Mr........")

B1 = Button(root, text='Print complete', command=print_me).pack()
B2 = Button(root, text='Print Selected', command=print_selected).pack()
B3 = Button(root, text='Clear', command=clear).pack()
root.mainloop()