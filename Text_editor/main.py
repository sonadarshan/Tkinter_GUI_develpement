from tkinter import *
from Text_editor import Filemenu
from Text_editor import Editmenu
from Text_editor import Thememenu

root = Tk()
root.title("TYPO")
text_area = Text(root, undo=True)
text_area.pack(fill=BOTH, expand=1)
# Create the main menu
main_menu = Menu()
root.config(menu=main_menu)
# Create the filemenu
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=lambda: Filemenu.new_file(text_area))
file_menu.add_command(label='Open', command=lambda: Filemenu.choose_file(text_area))
file_menu.add_separator()
file_menu.add_command(label='Save', command=lambda: Filemenu.save_file(text_area))
file_menu.add_command(label='Save as', command=lambda: Filemenu.save_as_file(text_area))
file_menu.add_command(label='Exit', command=root.quit)
file_menu.add_separator()
# Creating edit menu
edit_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo', command=lambda: Editmenu.undo(text_area))
edit_menu.add_command(label='Redo', command=lambda: Editmenu.redo(text_area))
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=lambda: Editmenu.cut_text(text_area))
edit_menu.add_command(label='Copy', command=lambda: Editmenu.copy_text(text_area))
edit_menu.add_command(label='Paste', command=lambda: Editmenu.paste_text(text_area))
edit_menu.add_separator()
# Creating theme menu
theme_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='Theme', menu=theme_menu)
theme_menu.add_command(label='Background', command=lambda: Thememenu.change_color(text_area))
root.mainloop()