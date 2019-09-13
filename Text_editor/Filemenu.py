from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def choose_file(text_area):
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


def save_as_file(text_area):
    global current_open_file
    result = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(("text files", '.txt'), ("all files", '.*')))
    if result is None:
        return
    current_open_file = result.name
    result.write(text_area.get(1.0, END))
    messagebox.showinfo('Success', 'File saved successfully')
    result.close()


def save_file(text_area):
    global current_open_file
    if current_open_file == "new_file.txt":
        save_as_file()
    else:
        file = open(current_open_file, 'w+')
        file.write(text_area.get(1.0, END))
        file.close()


def new_file(text_area):
    global current_open_file
    if len(text_area.get(1.0, END))>0:
        answer = messagebox.askquestion('Save', "Do you want to save the changes")
        if answer == 'yes':
            save_file()
    text_area.delete(1.0, END)
    current_open_file = 'new_file.txt'



