from tkinter import *
import tkinter.messagebox as tmsg
bishnu_root = Tk()
bishnu_root.geometry("540x540")
bishnu_root.title("Bishnu")

# photo = PhotoImage(file="Screenshot (12).png")
# tilak_label = Label(image=photo)
# tilak_label.pack()

# impotant label options

# text-adds the Text
# bd-background
# fg-foreground

# font-sets the font
# font=("comicsansms",19,"bold")
# font=("comicsansms 19 bold")

# padx - x padding
# pady - y padding
# refief - border styling - SUNKEN,RAISED,GROOVE,RIDGE


# title_label = Label(text='''Bishnu datt badu''',bg = "red",padx = 23,pady=45,font=("comicsansms 19 bold"),borderwidth=3,relief=SUNKEN)

# important pack option
# anchor = direction
# side = top bottom left right
# fill 
# padx
# pady


# title_label.pack(fill=X,anchor=CENTER)   

# f1 = Frame(bishnu_root,bg="grey",borderwidth=6,relief=SUNKEN)
# f1.pack(side = LEFT,fill=Y)

# f2=Frame(bishnu_root,bg="grey")
# f2.pack(side=TOP,fill=X)


# l1=Label(f1,text="Project Tkinter")
# l1.pack(pady=42)

# l2=Label(f2,text="hello world!!")
# l2.pack()

# def hello():
#     print("hello baby")

# b1= Button(f2,fg='red',text = "Print Now",command=hello)
# b1.pack(side=LEFT, padx=8,pady=5)

# b2= Button(bishnu_root,fg='red',text = "Print Now")
# b2.pack(side=BOTTOM, padx=8,pady=5)

# b3= Button(f2,fg='red',text = "Print Now")
# b3.pack(side=RIGHT, padx=8,pady=5)

# b4= Button(f2,fg='red',text = "Print Now")
# b4.pack(side=RIGHT, padx=8,pady=5)

# user = Label(bishnu_root,text="Username")
# password= Label(bishnu_root,text="password")
# user.grid()
# password.grid(row = 1)

# variable classes in tkinter
# BooleanVar DoubleVar, IntVar, StringVar


# uservalue= StringVar()
# passvalue= StringVar()

# userentry=Entry(bishnu_root,textvariable= uservalue)
# passentry=Entry(bishnu_root,textvariable= passvalue)

# userentry.grid(row=0,column=1)
# passentry.grid(row=1,column=1)

# def getvalue():
#     print(uservalue.get())
#     print(passvalue.get())

# Button(bishnu_root,text="Submit",command=getvalue).grid(row=3,column=1)

# def getvals():
#     with open("records.txt","a") as f:
#         f.write(f"{nameentry.get(),phoneentry.get(),genderentry.get(),emergencyentry.get(),paymententry.get(),foodservicevalue.get()}\n")


# Label(bishnu_root,text="welcome to Bishnu Company",pady=6,font="comicsansms 13 bold").grid(row=0,column = 3)
# name = Label(bishnu_root,text="Name")
# phone = Label(bishnu_root,text='Phone')
# gender = Label(bishnu_root,text='Gender')
# emergencycontact = Label(bishnu_root,text='Emergency Contact')
# paymentmode = Label(bishnu_root,text='Payment Mode')

# name.grid(row=1,column=2)
# phone.grid(row=2,column=2)
# gender.grid(row=3,column=2)
# emergencycontact.grid(row=4,column=2)
# paymentmode.grid(row=5,column=2)


# namevalue=StringVar()
# phonevalue=StringVar()
# gendervalue=StringVar()
# emergencyvalue=StringVar()
# paymentvalue=StringVar()
# foodservicevalue=BooleanVar()

# nameentry = Entry(bishnu_root,textvariable="namevalue")
# phoneentry = Entry(bishnu_root,textvariable="phonevalue")
# genderentry = Entry(bishnu_root,textvariable="gendervalue")
# emergencyentry = Entry(bishnu_root,textvariable="emergencyvalue")
# paymententry = Entry(bishnu_root,textvariable="paymentvalue")


# nameentry.grid(row=1,column=3)
# phoneentry.grid(row=2,column=3)
# genderentry.grid(row=3,column=3)
# emergencyentry.grid(row=4,column=3)
# paymententry.grid(row=5,column=3)

# foodservice=Checkbutton(bishnu_root,text="want to prebook your meal?",variable="foodservicevalue")
# foodservice.grid(row=6,column=3)





# Button(text="Submit",command=getvals).grid(row=7,column=3)

# CANVAS
# canvas_width= 800
# canvas_height=400
# bishnu_root.geometry(f"{canvas_width}x{canvas_height}")
# can_widget= Canvas(bishnu_root,width=canvas_width,height=canvas_height)
# can_widget.pack()

# the line goes from the point x1,y1 t0 x2,y2
# can_widget.create_line(0,0,800,400,fill="green")
# can_widget.create_line(0,400,800,0,fill="green")


# can_widget.create_rectangle(100,0,600,400,fill="red")
# can_widget.create_text(200,200,text="BISHNU")
# can_widget.create_oval(100,0,600,300)

# def bishnu(event):
#     print("You clicked on the button")

# widget=Button(bishnu_root,text="Click me")
# widget.pack()
# widget.bind('<Button-1>',bishnu)
# widget.bind('<Double-1>',quit)


# def myfunc():
#     print("its me")
#     a=tmsg.showinfo("Help","I am here ")
mymenu = Menu(bishnu_root)
# mymenu.add_command(label="File",command = myfunc)
mymenu.add_command(label="Exit",command = quit)
bishnu_root.config(menu=mymenu)

# def myfunc():
#     pass

# yourmenu = Menu(bishnu_root)
# m1=Menu(yourmenu,tearoff=0)
# m1.add_command(label="save",command=myfunc)
# m1.add_command(label="save As",command=myfunc)
# m1.add_separator()
# m1.add_command(label="Print",command=myfunc)
# m1.add_command(label="Exit",command=quit)
# yourmenu.add_cascade(label="File",menu=m1)

# bishnu_root.configure(menu= yourmenu)
# def rate():
#     tmsg.askquestion("Rate","are you fine?")





# help_menu=Menu(bishnu_root)
# help_menu.add_command(label="file",command=myfunc)
# help_menu.add_command(label="Rate us",command=rate)
# m1=Menu(help_menu,tearoff=0)
# m1.add_command(label="lorem",command=myfunc)
# help_menu.add_cascade(label="help",menu=m1)

# bishnu_root.configure(menu = help_menu)

# myslider=Scale(bishnu_root,from_=0,to=455)
# myslider.pack()
  
# myslider1=Scale(bishnu_root,from_=100,to=200,orient=HORIZONTAL,tickinterval=50)
# myslider1.pack()


# var= IntVar()

# var.set(1)

# Label(bishnu_root,text = "what would you like to have?",font="lucida 19 bold",justify=LEFT,padx=14).pack()

# radio= Radiobutton(bishnu_root,text="Dosa",padx=14,variable=var,value=1).pack(anchor=W)
# radio= Radiobutton(bishnu_root,text="Idly",padx=14,variable=var,value=2).pack(anchor=W)
# radio= Radiobutton(bishnu_root,text="Parathe",padx=14,variable=var,value=3).pack(anchor=W)
# radio= Radiobutton(bishnu_root,text="Samosa",padx=14,variable=var,value=4).pack(anchor=W)

# def order():
#     tmsg.showinfo("you have ordered",f"{var.get()}")


# Button(text="Order Now",command=order).pack()
# def add():
#     global i
#     lbx.insert(ACTIVE,f"{i}")
#     i+=1

# i=0
# scrollbar = Scrollbar(bishnu_root, orient="vertical")
# lbx=Listbox(bishnu_root,yscrollcommand=scrollbar.set)
# scrollbar.config(command=lbx.yview)
# # lbx.pack()

# lbx.insert(END,"First item of our listbox")
# scrollbar.pack(side="right", fill="y")
# lbx.pack( expand=True)
# Button(bishnu_root,text="Add Item",command=add).pack()

# For connecting scroll bar
# 1.widget(yscrollcommand=scrollbar.set)
# 2.scrollbar.config(command=widget.yview)

# scrollbar=Scrollbar(bishnu_root)
# scrollbar.pack(side="right",fill="y")


# lb = Listbox(bishnu_root,yscrollcommand = scrollbar.set)
# lb.pack(expand=TRUE)
# for i in range(344):
#     lb.insert(END,f"Item {i}")
    
# scrollbar.config(command=lb.yview)




# def upload():
#     statusvar.set("Busy..")
#     sbar.update()
#     import time
#     time.sleep(2)
#     statusvar.set("Ready")

# statusvar = StringVar()
# statusvar.set("Ready")

# sbar = Label(bishnu_root,textvariable=statusvar,relief=SUNKEN,anchor="w")
# sbar.pack(fill=X,side=BOTTOM)
# Button(bishnu_root,text="Upload",command=upload).pack()












bishnu_root.mainloop()
