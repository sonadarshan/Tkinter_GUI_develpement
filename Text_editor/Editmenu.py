from tkinter import *


def copy_text(text_area):
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.selection_get())


def cut_text(text_area):
    copy_text(text_area)
    text_area.delete('sel.first', 'sel.last')


def paste_text(text_area):
    text_area.insert(INSERT, text_area.clipboard_get())


def undo(text_area):
    text_area.edit_undo()


def redo(text_area):
    text_area.edit_redo()
