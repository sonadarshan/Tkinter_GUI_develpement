from tkinter import *
from tkinter import filedialog

def choose_file():
    result = filedialog.askopenfile(initialdir='/', title='Select file', filetypes =(("text files", '.txt'), ( "all files", '.*')))
    print(result)
    for c in result:
        print(c)

root = Tk()
root.title("Browse to choose your file")
root.geometry('400x400')
b1 = Button(root, text='Click', command=choose_file)
b1.pack()

root.mainloop()