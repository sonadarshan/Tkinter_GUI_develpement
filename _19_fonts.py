from tkinter import *
from tkinter.font import Font
from tkinter import font

root = Tk()
root.title("Fonts")
root.geometry("600x600+100+100")

my_font = Font(family='Times New Roman', size=16, weight='bold', slant='italic', underline=1, overstrike=0)
label = Label(root, text='Hello ji',font=my_font).pack()
fonts = list(font.families())
print(fonts)
root.mainloop()