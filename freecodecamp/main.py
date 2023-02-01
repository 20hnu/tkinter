from tkinter import *


root = Tk()
root.title("Python")
root.geometry("540x540")

menu=Menu(root)
menu.add_command(label="Exit",command=quit)
root.configure(menu=menu)
mylabel = Label(root,text="hello world",padx=1080,pady=30,font=("Arial",25),fg="red",bg="blue").pack()

root.mainloop()