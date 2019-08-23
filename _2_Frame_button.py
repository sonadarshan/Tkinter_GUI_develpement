from tkinter import *

root = Tk()

frame = Frame(root, width=1000, height=1000)
# This is used to create a button
button1 = Button(frame, text="Left")
button2 = Button(frame, text="Centre")
button3 = Button(frame, text='Right')
# To align the created widgets
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
frame.pack()

bottomframe = Frame(root)
# Bottom allignement
button4 = Button(bottomframe, text="Bottom")
button4.pack()
bottomframe.pack(side=BOTTOM)

root.mainloop()
