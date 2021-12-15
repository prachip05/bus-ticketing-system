from tkinter import *
from tkinter import messagebox
import subprocess
root=Tk()

root.title('ADMIN Login')

root.configure(background='light grey')
a=PhotoImage(file="g.gif")
Label(root,image=a).grid(row=0,column=0,columnspan=8)


def check():   
    ''' Check Button for Login Window '''
    global un, pwd, root
    
    
    u=un.get()
    p=pwd.get()
    if 'prachi'==u and 'pradhya16'==p:
        
        root.destroy()
        subprocess.call("python add.py") 
        
       
       
    else:
        messagebox.showerror('ERROR','Wrong ID or Password :Please try again')
        root.mainloop()



        # login.close()







    
Label(root,text='ADMIN LOGIN (ADD BUS)',font=('arial',20,'bold'),bd=7,fg='red',bg='light grey').grid(row=1,column=0,columnspan=8)

Label(root,text='---------------------------------------------------------------------',bg='light grey').grid(row=3,column=0,columnspan=5)
Label(root, text='Username',font=('arial',10,'bold'),bg='light grey').grid(row=4, column=1)
un=Entry(root,bd=2,width=10)
un.grid(row=4, column=2)
Label(root, text='Password',font=('arial',10,'bold'),bg='light grey').grid(row=5, column=1)
pwd=Entry(root,width=10,bd=2, show="*")
pwd.grid(row=5, column=2)
Label(root,text='').grid(row=6,column=0,columnspan=5)
Button(root,width=6,text='Login',font=('arial',10,'bold'),bd=4,bg='dark grey',command=check).grid(row=7, column=1)
Button(root,width=6,text='Close',font=('arial',10,'bold'),bd=4,bg='dark grey',command=root.destroy).grid(row=7, column=2)


root.title("BUS TICKETING SYSTEM")



root.mainloop()
