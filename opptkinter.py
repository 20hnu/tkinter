from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        Label(self,text="hello world",textvariable=self.var,relief = SUNKEN,anchor="w").pack(side=BOTTOM,fill="x")

    def click(self):
        print("Button clicked")
    def createbutton(self,inputtext):
        Button(text=inputtext,command=self.click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("hello")
    window.mainloop()