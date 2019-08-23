from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Extreme")
def new_file():
    print('New file created')
def close_file():
    print("File closed")
def edit_file():
    print("File bieng edited")





# Initially declae a menu object
main_menu = Menu(root)
root.config(menu=main_menu)
# Adding different menus
# 1
file_menu = Menu(main_menu)
# Adding a menu to the menu
main_menu.add_cascade(label='File', menu=file_menu)
# Adding dropdowns to the file menu (commands the direct functionalities)
file_menu.add_command(label='New_file', command=new_file)
file_menu.add_command(label='Close_file', command=close_file)
# Introduces a line
file_menu.add_separator()
# Introducing menu under a menu
new_menu = Menu(file_menu)
new_menu.add_cascade(label='Python')
new_menu.add_separator()
new_menu.add_cascade(label='Robot')
file_menu.add_cascade(label='types', menu=new_menu)

# 2
edit_menu = Menu(main_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='edit', command=edit_file)



root.mainloop()