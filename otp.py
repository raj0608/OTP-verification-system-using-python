from twilio.rest import Client
import tkinter as tk
from tkinter import messagebox
import random
otp=random.randint(1000,10000)
otp=str(otp)

def check():
    userentry=y.get()
    if otp==userentry:
        messagebox.showinfo("info",'login successful')
    elif otp!=userentry:
        messagebox.showinfo("info","wrong OTP")

def sendsms():
    number=x.get()
    
    client = Client('Account SID','Auth Token') 
    
    client.messages.create(from_='+15203379216',to=number , body="Your OTP is:"+otp)
    
    messagebox.showinfo("info","OTP sent :)")
    root.destroy()
    win=tk.Tk()
    win.geometry("300x200")
    global y
    y=tk.StringVar()
    l2=tk.Label(win,text="Enter OTP",bg="black",fg="white")
    l2.place(x=15,y=5,width=250)
    e2=tk.Entry(win,textvariable=y)
    e2.place(x=15,y=30,height=30,width=250)
    b1=tk.Button(win,text="Submit",bg="green",fg="white",command=check)
    b1.place(x=100,y=80)
    

    

root=tk.Tk()
root.configure(bg="black")
root.geometry("300x200")
root.title("OTP verification system")
global x
x=tk.StringVar()
l1=tk.Label(root,text="Enter your phone no.",bg="black",fg="white")
l1.place(x=15,y=5,width=250)
e1=tk.Entry(root,textvariable=x)
e1.place(x=15,y=30,height=30,width=250)
b=tk.Button(root,text="Send OTP",bg="green",fg="white",command=sendsms)
b.place(x=100,y=80)
root.mainloop()



