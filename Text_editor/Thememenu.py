from tkinter import colorchooser


def change_color(text_area):
    clr = colorchooser.askcolor(title='Select color')
    # It returns a tuple with RGB values at 0th index and color hexvalue at 1st index
    text_area.configure(background=clr[1])
