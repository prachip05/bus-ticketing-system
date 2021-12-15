from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
import subprocess
root=Tk()
root.title("Bus Admission")


con=sqlite3.connect('BUS DETAIL')
cur=con.cursor()

cur.execute("create table if not exists cust(bno varchar2(10),source varchar2(10),dest varchar2(10),bt varchar2(10),d varchar2(10),td varchar2(5),ta varchar(5),fare INT(5),seats INT(2))") 
Label(root,text="BUS ADDITION",font='arial 20 bold',bd=1).grid(row=0,column=0,sticky=E+W)
Label(root,text=" MODULE",font='arial 20 bold',bd=1).grid(row=0,column=1,sticky=E+W)
Label(root,text="----------------",font='arial 20 bold',bd=1).grid(row=1,column=0,sticky=E+W)
Label(root,text="----------------",font='arial 20 bold',bd=1).grid(row=1,column=1,sticky=E+W)
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()


Label(root,text="Bus Operator :",font='calibri 20').grid(row=2,column=0)
Label(root,text="Source City :",font='calibri 20').grid(row=3,column=0)
Label(root,text="Destination City :",font='calibri 20').grid(row=4,column=0)
Label(root,text="Bus Type :",font='calibri 20').grid(row=5,column=0)
Label(root,text="Running Date(DD-MM-YYYY) :",font='calibri 20').grid(row=6,column=0)
Label(root,text="Departure Time(24Hr) :",font='calibri 20').grid(row=7,column=0)
Label(root,text="Arrival Time(24Hr) :",font='calibri 20').grid(row=8,column=0)
Label(root,text="Fare :",font='calibri 20').grid(row=9,column=0)
Label(root,text="Total Seats :",font='calibri 20').grid(row=10,column=0)

global bno,source,dest,bt,d,td,ta,fare,seats
bno=Entry(root)
source=Entry(root)
dest=Entry(root)
bt=ttk.Combobox(root,width=15,font='calibri 10',textvariable=v1)
bt.grid(row=5,column=1,sticky=W)
v1.set('      --Please Select--')
bt['values']=['AC Sleeper','AC Seater','Non AC Sleeper','Non AC Seater']
d=Entry(root)
td=Entry(root)
ta=Entry(root)
fare=Entry(root)
seats=Entry(root)



bno.grid(row=2,column=1)
source.grid(row=3,column=1)
dest.grid(row=4,column=1)
d.grid(row=6,column=1)
td.grid(row=7,column=1)
ta.grid(row=8,column=1)
fare.grid(row=9,column=1)
seats.grid(row=10,column=1)


def insert():
    try:
        cur.execute("insert into cust values(?,?,?,?,?,?,?,?,?)",(bno.get(),source.get(),dest.get(),bt.get(),d.get(),td.get(),ta.get(),fare.get(),seats.get()))
        con.commit()
        messagebox.showinfo('Success','The record has been inserted successfully')
    except:
        messagebox.showerror('Error!','An entry with same bill no already exists!')
    
            
def exitpls():
    root.destroy()
    subprocess.call("python pro.py")
    
    
Label(root,text="                       ",font='arial 20 bold',bd=1).grid(row=11,column=0,sticky=E+W)
Button(root,text='Insert',command=insert,bd=5,bg='dark grey',font=('arial',16,'bold')).grid(row=12,column=0)
Button(root,text='Home',font=('arial',16,'bold'),bd=5,bg='dark grey',command=exitpls).grid(row=12,column=1)


root.mainloop()



