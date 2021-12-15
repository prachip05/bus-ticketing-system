from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
import subprocess
root=Tk()
root.title("Bus Search")



Label(root,text="BUS SEARCH",font='arial 20 bold',bd=1).grid(row=1,column=0,sticky=E+W)
Label(root,text=" MODULE",font='arial 20 bold',bd=1).grid(row=1,column=1,sticky=E+W)
Label(root,text="----------------",font='arial 20 bold',bd=1).grid(row=2,column=0,sticky=E+W)
Label(root,text="----------------",font='arial 20 bold',bd=1).grid(row=2,column=1,sticky=E+W)
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()



b=PhotoImage(file="f.gif")
Label(root,image=b).grid(row=0,column=0,columnspan=8)

Label(root,text="Source City :",font='calibri 20').grid(row=3,column=0)
Label(root,text="Destination City :",font='calibri 20').grid(row=4,column=0)
Label(root,text="Bus Type :",font='calibri 20').grid(row=5,column=0)
Label(root,text="Running Date(DD-MM-YYYY) :",font='calibri 20').grid(row=6,column=0)


global source,dest,bt,d
source1=Entry(root)
dest1=Entry(root)
bt1=ttk.Combobox(root,width=15,font='calibri 10',textvariable=v1)
bt1.grid(row=5,column=1,sticky=W)
v1.set('--Please Select--')
bt1['values']=['AC Sleeper','AC Seater','Non AC Sleeper','Non AC Seater','All Types']
d1=Entry(root)
source1.grid(row=3,column=1)
dest1.grid(row=4,column=1)
d1.grid(row=6,column=1)


def show():
    s1=str(source1.get())
    s2=str(dest1.get())
    s3=str(bt1.get())
    s4=str(d1.get())
    if s1=="" or s2=="" or s4=="" or s3=="--Please Select--":
        messagebox.showerror('Error!','Invalid Entry!')
    else:
        
        conn=sqlite3.connect('BUS DETAIL')
        cur=conn.cursor()
        if s3 == "All Types":
            cur.execute('select * from cust where source=? and dest=? and d=?',(s1,s2,s4))
            x=cur.fetchall()
        else:
            cur.execute('select * from cust where source=? and dest=? and bt=? and d=?',(s1,s2,s3,s4))
            x=cur.fetchall()
        
        new=Tk()
        new.geometry("1400x1000")
        new.title("All Records")
        new.configure(background='powder blue')
        i=0
        Label(new,text="| BUS OPERATOR |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=0)
        Label(new,text="|  BUS TYPE |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1)
        Label(new,text="|   DATE    |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=2)
        Label(new,text="| DEPARTURE  TIME |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=3)
        Label(new,text="| ARRIVAL TIME |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=4)
        Label(new,text="| FARE |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=5)
        Label(new,text="| SEATS LEFT |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=6)
        Label(new,text="| SELECT |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=7)
        
        var=IntVar()
        for i in range (0,len(x)):
            Label(new,text=x[i][0],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=0)
            Label(new,text=x[i][3],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=1)
            Label(new,text=x[i][4],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=2)
            Label(new,text=x[i][5],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=3)
            Label(new,text=x[i][6],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=4)
            Label(new,text=x[i][7],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=5)
            Label(new,text=x[i][8],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=6)
            R1=Radiobutton(new,text="",variable=var,value=i+1,command=select,bg='powder blue').grid(row=i+1,column=7)
        Button(new,text='PROCEED',command=go,bd=5,bg='dark grey',font=('arial',16,'bold')).grid(row=15,column=7)
        Button(new,text='BACK',command=exit1,bd=5,bg='dark grey',font=('arial',16,'bold')).grid(row=16,column=7)
        label=Label(new)
        label.pack()
       
        new.mainloop()

def go():
    subprocess.call("python customer.py")
    new.destroy()
    
def select():
    select=str(var.get())
    label.config(text=select)

def exit1():
    root.destroy()
    subprocess.call("python search.py")            
def exitpls():
    root.destroy()
    subprocess.call("python pro.py")
    
Label(root,text="                       ",font='arial 20 bold',bd=1).grid(row=11,column=0,sticky=E+W)
Button(root,text='Search',command=show,bd=5,bg='dark grey',font=('arial',16,'bold')).grid(row=12,column=0)
Button(root,text='Back',font=('arial',16,'bold'),bd=5,bg='dark grey',command=exitpls).grid(row=12,column=1)


root.mainloop()



