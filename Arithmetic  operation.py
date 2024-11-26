from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("Centered Buttons Calculator")
root.geometry("640x740")
root.configure(bg="#333333")
canvas=Canvas(root,bg="gray16", height=200,width=400)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\sakshi dewangan\\OneDrive\\Desktop\\loginimage2.jpg"))
background_label=Label(root,image=image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
title=Label(root,text="Arithmetic Operations", font=("times new roman",25,"bold"),bg="powderblue", fg="dark green",bd=10)
title.grid(row=0, column=0, columnspan=3, pady=20)
title.place(x=0,y=0,relwidth=1)

#calculator frame
add_frm=Frame(root,bg="#ff6699", relief="ridge")
add_frm.place(x=450,y=200)
add_frm.configure(bd=10)

one=StringVar()
two=StringVar()
three=StringVar()

first=Label(add_frm,text="Enter First No:", font=("times new roman",15,"bold"),bg="#ff6699", fg="dark green").grid(row=1,column=0,pady=20, sticky="e")
first=Entry(add_frm, font=("times new roman",12), textvariable=one).grid(row=1,column=1,pady=20)
second=Label(add_frm,text="Enter Second No:", font=("times new roman",15,"bold"),bg="#ff6699", fg="dark green").grid(row=2,column=0,pady=20)
second=Entry(add_frm, font=("times new roman",12), textvariable=two).grid(row=2,column=1,padx=10,pady=20)
txtres=Entry(add_frm, font=("times new roman",12),textvariable=three).grid(row=3,columnspan=2,pady=20)
res1=Entry(add_frm,width=20,textvariable=three)
def add():
    a=one.get()
    b=two.get()
    c=int(a)+int(b)
    three.set(c)
    messagebox.showinfo("Addition",c)
btn1=Button(text="+", font=("Arial" ,15,"bold"), width=3, height=1, relief="ridge", fg="deeppink2", bg="black",command=add).grid(row=4,pady=10)

def sub():
    a=int(one.get())
    b=int(two.get())
    c=int(a)-int(b)
    three.set(c)
    messagebox.showinfo("subtraction",c)
btn2=Button(text="-", font=("Arial" ,15,"bold"), width=3, height=1, relief="ridge", fg="deeppink2", bg="black", command=sub).grid(row=5,pady=10)

def multi():
    a=one.get()
    b=two.get()
    c=int(a)*int(b)
    three.set(c)
    messagebox.showinfo("multiply",c)
btn3=Button(text="*", font=("Arial" ,15, "bold"), width=3, height=1, relief="ridge",fg="deeppink2", bg="black", command=multi).grid(row=6,pady=10)

def div():
    a=one.get()
    b=two.get()
    c=int(a)/int(b)
    three.set(c)
    messagebox.showinfo("divide",c)
btn4=Button(text="/", font=("Arial", 15, "bold"), width=3, height=1, relief="ridge", fg="deeppink2", bg="black", command=div).grid(row=7,pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
