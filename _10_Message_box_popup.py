from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Popcorn popup")
root.geometry('500x500')


def showinfor():
    # We can use messagebox.showinfo or messagebox.showerror etc...
    messagebox.showinfo("Confirm please", "Are you sure want to exit")


def askqtn():
    # There are fn like asyesno, asyesnocancel etc...askyesnocancel returns true false and none
    answer = messagebox.askquestion('Exit', "Are you sure want to exit!....")
    if answer == 'yes':
        root.quit()
    #For no just click it will come back after a single click message box will go out


b1 = Button(root, text="check it bro", command=showinfor)
b2 = Button(root, text="Exit", command=askqtn)
b1.pack(side=TOP)
b2.pack(side=BOTTOM)

root.mainloop()