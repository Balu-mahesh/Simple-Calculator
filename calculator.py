#Python program of a Basic calculator using tkinter.
from tkinter import *
from tkinter import messagebox

val=""

def button_clicked(number):
    global val
    val=val+str(number)
    data.set(val)

def button_clear():
    global val
    val=""
    data.set("")

def result():
    global val
    try:
        sumup=str(eval(val))
        data.set(sumup)
        val=sumup
    except:
        messagebox.showinfo("Warning","Division by Zero not possible !")
        button_clear()

def back():
    global val
    val=val[0:-1]
    data.set(val)

root=Tk()
root.title("Calculator")

data=StringVar()
l1=Label(root,textvariable=data,height=4,width=35,bg="#3d3d40",fg="white",anchor="se",font=("Arial","12"))
l1.grid(row=1,column=1,columnspan=4)

clear=Button(root,text="C",width=7,height=3,font=("Arial",12,"bold"),bg="#61c2ed",fg="white",bd=0,command=button_clear)
clear.grid(row=2,column=1,columnspan=1)
backspace=Button(root,text="<<",width=7,height=3,font=("Arial",12,"bold"),bg="#61c2ed",fg="white",bd=0,command=back)
backspace.grid(row=2,column=2,columnspan=1)
per=Button(root,text="%",width=7,height=3,font=("Arial",12,"bold"),bg="#61c2ed",fg="white",bd=0,command=lambda:button_clicked("%"))
per.grid(row=2,column=3,columnspan=1)
div=Button(root,text="/",width=7,height=3,font=("Arial",12,"bold"),bg="#189cd6",fg="white",bd=0,command=lambda:button_clicked("/"))
div.grid(row=2,column=4,columnspan=1)

b7=Button(root,text="7",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(7))
b7.grid(row=3,column=1,columnspan=1)
b8=Button(root,text="8",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(8))
b8.grid(row=3,column=2,columnspan=1)
b9=Button(root,text="9",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(9))
b9.grid(row=3,column=3,columnspan=1)
pro=Button(root,text="x",width=7,height=3,font=("Arial",12,"bold"),bg="#189cd6",fg="white",bd=0,command=lambda:button_clicked("*"))
pro.grid(row=3,column=4,columnspan=1)

b4=Button(root,text="4",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(4))
b4.grid(row=4,column=1,columnspan=1)
b5=Button(root,text="5",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(5))
b5.grid(row=4,column=2,columnspan=1)
b6=Button(root,text="6",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(6))
b6.grid(row=4,column=3,columnspan=1)
minus=Button(root,text="-",width=7,height=3,font=("Arial",12,"bold"),bg="#189cd6",fg="white",bd=0,command=lambda:button_clicked("-"))
minus.grid(row=4,column=4,columnspan=1)

b1=Button(root,text="1",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(1))
b1.grid(row=5,column=1,columnspan=1)
b2=Button(root,text="2",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(2))
b2.grid(row=5,column=2,columnspan=1)
b3=Button(root,text="3",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(3))
b3.grid(row=5,column=3,columnspan=1)
plus=Button(root,text="+",width=7,height=7,font=("Arial",12,"bold"),bg="#189cd6",fg="white",bd=0,command=lambda:button_clicked("+"))
plus.grid(row=5,column=4,columnspan=1,rowspan=2)

dot=Button(root,text=".",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked("."))
dot.grid(row=6,column=1,columnspan=1)
b0=Button(root,text="0",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=lambda:button_clicked(0))
b0.grid(row=6,column=2,columnspan=1)
equal=Button(root,text="=",width=7,height=3,font=("Arial",12,"bold"),bd=0,command=result)
equal.grid(row=6,column=3,columnspan=1)

root.mainloop()
