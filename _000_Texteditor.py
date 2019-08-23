from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

root = Tk()
root.title("Extreme note pad")


def choose_file():
    global current_open_file
    result = filedialog.askopenfile(initialdir='/', title='Select file', filetypes=(("text files", '.txt'), ("all files", '.*')))
    if result is not None:
        text_area.delete(1.0, END)
        current_open_file = result.name
    try:
        for line in result:
            text_area.insert(END, line)
    except:
        messagebox.showerror('Error', 'The file cant be opened')


def save_as_file():
    global current_open_file
    result = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(("text files", '.txt'), ("all files", '.*')))
    if result is None:
        return
    current_open_file = result.name
    result.write(text_area.get(1.0, END))
    messagebox.showinfo('Success', 'File saved successfully')
    result.close()


def save_file():
    global current_open_file
    if current_open_file == "new_file.txt":
        save_as_file()
    else:
        file = open(current_open_file, 'w+')
        file.write(text_area.get(1.0, END))
        file.close()


def new_file():
    global current_open_file
    if len(text_area.get(1.0, END))>0:
        answer = messagebox.askquestion('Save', "Do you want to save the changes")
        if answer == 'yes':
            save_file()
    text_area.delete(1.0, END)
    current_open_file = 'new_file.txt'


def exit_file():
    answer = messagebox.askquestion('Exit', "Are you sure want to exit!....")
    if answer == 'yes':
        root.quit()


# Create a text area
text_area = Text(root, undo=True)
text_area.pack(fill=BOTH, expand=1)
# Create the main menu
main_menu = Menu()
root.config(menu=main_menu)
# Create the filemenu
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=choose_file)
file_menu.add_separator()
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save as', command=save_as_file)
file_menu.add_command(label='Exit', command=exit_file)
file_menu.add_separator()


def copy_text():
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.selection_get())


def cut_text():
    copy_text()
    text_area.delete('sel.first', 'sel.last')


def paste_text():
    text_area.insert(INSERT, text_area.clipboard_get())


def undo():
    text_area.edit_undo()


def redo():
    text_area.edit_redo()


# Create the editmenu
edit_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo', command=undo)
edit_menu.add_command(label='Redo', command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_separator()


def change_color():
    clr = colorchooser.askcolor(title='Select color')
    # It returns a tuple with RGB values at 0th index and color hexvalue at 1st index
    text_area.configure(background=clr[1])


# Creating the Theme menu
theme_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='Theme', menu=theme_menu)
theme_menu.add_command(label='Background', command=change_color)
root.mainloop()