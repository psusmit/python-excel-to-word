# imports
from tkinter import *
import tkinter as tk


# all functions go here
def submit1():
    import second
    return e1.get(),e2.get(),e3.get(),var.get()


master = tk.Tk() 
master.title('Initial information')
Label(master, text='Name of Work: ').grid(row=0) 
Label(master, text='Head of Account').grid(row=1) 
Label(master, text='Major Head').grid(row=2) 
Label(master, text='Minor Head').grid(row=3) 
e1 = Entry(master) 
e2=Entry(master)
e3=Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=2, column=1) 
e3.grid(row=3, column=1) 
var = StringVar(master)
option = OptionMenu(master, var, "l", "rural", "urban")
option.place(x=10,y=80)
button = tk.Button(master, text='Submit', width=15,command=submit1)
button.grid(row=4,column=1)
close=tk.Button(master,text='Close',command=master.destroy)
close.grid(row=4,column=2)


mainloop() 