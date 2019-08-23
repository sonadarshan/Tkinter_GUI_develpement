from tkinter import *

root = Tk()
root.title("Canvas line drawing")
root.geometry('1000x1000')

canvas = Canvas(root, width=200, height=200, bg='white')
canvas.pack()

# Drwaing a line
canvas.create_line(0, 0, 200, 100)
canvas.create_line(200, 100, 0, 200, fill='red')
# Drawing a arc
# extent is used to change the angle
canvas.create_arc(10, 0, 200, 200, extent=60 ,fill='blue')

root.mainloop()
