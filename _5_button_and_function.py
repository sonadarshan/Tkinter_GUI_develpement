from tkinter import *

root = Tk()

def check_login(name):
    print("Login verified"+name)


name = Label(root, text="Name")
password = Label(root, text="Password")
name_input = Entry()
pass_input = Entry()
login = Button(root, text='Login',command=lambda: check_login(str(name_input)))
name.grid(row=0, column=0)
password.grid(row=1, column=0)
name_input.grid(row=0, column=1)
pass_input.grid(row=1, column=1)
c = Checkbutton(root, text='Keep me logged in')
c.grid(columnspan=2)
login.grid(columnspan=3)

root.mainloop()