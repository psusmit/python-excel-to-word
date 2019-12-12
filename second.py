# imports
from tkinter import *
import tkinter as tk
srsList=[]
qlist=[]
# all functions go here
def addMore():
    
    master = tk.Tk()
    Label(master, text='Srs no.: ').grid(row=0) 
    Label(master, text='Quantity: ').grid(row=1) 
    e1 = Entry(master) 
    e2=Entry(master)
    e1.grid(row=0, column=1) 
    e2.grid(row=1, column=1) 
    srsList.append(e1.get())
    qlist.append(e2.get())
    moreButton=tk.Button(master,text='Add more data',command=addMore)
    moreButton.grid(row=2,column=0)
    submitButton=tk.Button(master,text='Close',command=master.destroy)
    submitButton.grid(row=2,column=1)
    master.mainloop()
    

master = tk.Tk()
master.geometry('200x100')
Label(master, text='Srs no.: ').grid(row=0) 
Label(master, text='Quantity: ').grid(row=1) 
e1 = Entry(master) 
e2=Entry(master)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
srsList.append(e1.get())
qlist.append(e2.get())
moreButton=tk.Button(master,text='Add more data',command=addMore)
moreButton.grid(row=2,column=0)
submitButton=tk.Button(master,text='Submit',command=master.destroy)
submitButton.grid(row=2,column=1)
master.mainloop()

