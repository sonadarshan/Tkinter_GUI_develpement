from tkinter import *
from tkinter import messagebox

root = Tk()


def check_login(name,password):
    if name == 'sona' and password == 'darshan':
        messagebox.showinfo("Hello "+name,"Login Successfull")


name = Label(root, text="Name")
password = Label(root, text="Password")
name_input = Entry()
pass_input = Entry()
name.grid(row=0, column=0)
password.grid(row=1, column=0)
name_input.grid(row=0, column=1)
pass_input.grid(row=1, column=1)
login = Button(root, text='login', command=lambda :check_login(name_input.get(),pass_input.get()))
login.grid(columnspan=3,)
c = Checkbutton(root, text='Keep me logged in')
c.grid(columnspan=2)

root.mainloop()