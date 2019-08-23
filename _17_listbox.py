from tkinter import *


def print_me():
    clickeditems = l.curselection()
    # Clickeditems top print only the index number
    print(clickeditems)
    # This prints the value stored in that item
    for item in clickeditems:
        print(l.get(item))


def delete_me():
    clickeditems = l.curselection()
    # This delets the value stored in that item
    for item in clickeditems:
        l.delete(item)


root = Tk()
# Select modes are BROWSE,SINGLE,MULTIPLE,EXTENDED
l = Listbox(root, width=30, height=10, selectmode=MULTIPLE)
l.insert(1, 'C++')
l.insert(2, 'Java')
l.insert(3, 'Python')
l.insert(4, 'Robot')
l.insert(5, 'C#')
l.pack()


B1 = Button(root, text='Print', command=print_me)
B2 = Button(root, text='Delete', command=delete_me)
B1.pack()
B2.pack()
root.mainloop()
