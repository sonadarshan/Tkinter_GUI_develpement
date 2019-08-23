from tkinter import *

root = Tk()
root.geometry('600x600')
root.title('Scaler')

slider = Scale(from_=0, to=100, orient=HORIZONTAL, length=200, width=10, sliderlength=50)
# To set the default slider to the centre of the window
slider.set(50)
slider.pack()
print(slider.get())
root.mainloop()