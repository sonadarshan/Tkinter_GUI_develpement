from tkinter import *


class Mybuttons:
    def __init__(self,master):
        master.title("Press The Button")
        master.geometry('300x300')
        self.printButton = Button(master, text='Print', command=self.printing)
        self.printButton.pack()
        self.quitButton = Button(master, text='Quit', command=master.quit)
        self.quitButton.pack()

    def printing(self):
        print("Printing")


root = Tk()
b = Mybuttons(root)
root.mainloop()