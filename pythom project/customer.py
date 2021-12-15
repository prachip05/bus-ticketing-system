from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
import subprocess
frame4=Tk()
frame4.title("Passenger details")
frame4.geometry('900x300')
frame4.configure(background='powder blue')
conn=sqlite3.connect('project_db')
c1=conn.cursor()
c1.execute('create table if not exists reserve(serial INT(10),name varchar(10),age INT(2),gender varchar(7))')
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()   
v8=StringVar()
v9=StringVar()
v10=StringVar()
v11=StringVar()
v12=StringVar()
v13=StringVar()
v14=StringVar()
v15=StringVar()
v16=StringVar()
v17=StringVar()
v18=StringVar()
v19=StringVar()
v20=StringVar()
v21=StringVar()
v22=StringVar()
v23=StringVar()
v24=StringVar()
v25=StringVar()
v26=StringVar()
v40=StringVar()
v41=StringVar()
v42=StringVar()
v43=StringVar()
v44=StringVar()
v45=StringVar()
v46=StringVar()
v47=StringVar()
v48=StringVar()
v49=StringVar()
v50=StringVar()
v51=StringVar()
v52=StringVar()
v53=StringVar()
v54=StringVar()
v55=StringVar()
v56=StringVar()
v57=StringVar()
v58=StringVar()
v59=StringVar()
v60=StringVar()
v61=StringVar()
v62=StringVar()
v63=StringVar()
v64=StringVar()
v65=StringVar()
v66=StringVar()
v67=StringVar()
v68=StringVar()
v69=StringVar()
v70=StringVar()

Label(frame4,text='SNo',font='arial 17',padx=20,bg='light grey',bd=4,relief=SUNKEN).grid(row=0,sticky=W)
Label(frame4,text='Name',font='arial 17',width=20,padx=20,bg='light grey',bd=4,relief=SUNKEN).grid(row=0,column=1,sticky=W)
Label(frame4,text='Age',font='arial 17',padx=20,bg='light grey',bd=4,relief=SUNKEN).grid(row=0,column=2,sticky=W)
Label(frame4,text='Sex',font='arial 17',width=8,padx=20,bg='light grey',bd=4,relief=SUNKEN).grid(row=0,column=3,sticky=W)


Label(frame4,text='1',font='arial 14 ',padx=20,bd=4,relief=SUNKEN,bg='light grey',pady=10).grid(row=1,sticky=W+E+N+S)
Label(frame4,text='2',font='arial 14 ',bg='light grey',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=2,sticky=W+E+N+S)
Label(frame4,text='3',font='arial 14 ',bg='light grey',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=3,sticky=W+E+N+S)
Label(frame4,text='4',font='arial 14 ',bg='light grey',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=4,sticky=W+E+N+S)
            
            
e2=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
e2.grid(row=1,column=1)

e3=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
e3.grid(row=2,column=1)

e4=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
e4.grid(row=3,column=1)

e5=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
e5.grid(row=4,column=1)

            

f2=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
f2.grid(row=1,column=2)

f3=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
f3.grid(row=2,column=2)

f4=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
f4.grid(row=3,column=2)

f5=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
f5.grid(row=4,column=2)

            
C1=ttk.Combobox(frame4,font='arial 17',textvariable=v17,width=10)
C1.grid(row=1,column=3)
C1['values']=['Male','Female']
v17.set('Select')

C2=ttk.Combobox(frame4,font='arial 17',textvariable=v18,width=10)
C2.grid(row=2,column=3)
C2['values']=['Male','Female']
v18.set('Select')

C3=ttk.Combobox(frame4,font='arial 17',textvariable=v19,width=10)
C3.grid(row=3,column=3)
C3['values']=['Male','Female']
v19.set('Select')

C4=ttk.Combobox(frame4,font='arial 17',textvariable=v20,width=10)
C4.grid(row=4,column=3)
C4['values']=['Male','Female']
v20.set('Select')

            

           

           

cb1=Checkbutton(frame4,variable=v47,bg='powder blue',width=5,onvalue=1)
cb1.grid(row=1,column=5)

cb2=Checkbutton(frame4,variable=v48,bg='powder blue',width=5,onvalue=1)
cb2.grid(row=2,column=5)

cb3=Checkbutton(frame4,variable=v49,bg='powder blue',width=5,onvalue=1)
cb3.grid(row=3,column=5)

cb4=Checkbutton(frame4,variable=v50,bg='powder blue',width=5,onvalue=1)
cb4.grid(row=4,column=5)

xxx=[]

def next1(xx,xxxx,xxxxx):

    messagebox.showinfo('Confirm','reservation successfull-pay at the office')
    global xxx
    a=[i.get() for i in xxx]
    a1=[i.get() for i in xx]
    a2=[i.get() for i in xxxx]
    a3=[i.get() for i in xxxxx]
    for i in a1:
        if i=='':
            break
        else:
            count = count+1
    
            
    for i in range(count):
        insert_into_reservation(a[0],a1[i],a2[i],a3[i])
        

def insert_into_reservation(a,b,c,d):
    a=[]
    a.append((str(a4),str(a5),str(a6),str(a7)))
    c1.executemany('insert into reservation values(?,?,?,?)',a)
    conn.commit()            
 
xx=[e2,e3,e4,e5]
xxxx=[f2,f3,f4,f5]
xxxxx=[v17,v18,v19,v20]
            
Button(frame4,text='RESERVE',relief='raised',bg="dark grey",padx=10,pady=10,font='Arial 17',command=lambda:next1(xx,xxxx,xxxxx)).grid(row=11,column=5,columnspan=1)

frame4.mainloop()
