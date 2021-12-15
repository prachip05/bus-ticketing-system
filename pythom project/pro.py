from tkinter import *
import subprocess
root=Tk()

root.title('welcome')
root.geometry("1800x1800")
root.configure(background='light grey')
def images():
  subprocess.call("python begin.py")  

   
   


      

#for new Window      
def welcome():
   
   
   subprocess.call("python search.py")  
   
  
   
   
def fun():
   owner=Toplevel()
   owner.geometry('1000x1300')
   owner.title('Contact us')
   owner.configure(background='black')
   c = PhotoImage(file = "pp.gif")
   Label(owner , image = c).place(x=400,y=0)
   Label(owner,text='OWNER:- PRACHI PANDEY',relief='raised',font='times 20 bold italic ').place(x=0,y=200)
   
   Label(owner,text='Email:- 191B187@juetguna.in',relief='raised',font='times 15 bold italic ').place(x=0,y=300)

   Label(owner,text='Mobile:- 6260008210',relief='raised',font='times 15 bold italic ').place(x=0,y=400)

   Label(owner,text='Address:- B-Girls Hostel,JUET,Guna,MP',relief='raised',font='times 15 bold italic ').place(x=0,y=500)

   
   
   owner.mainloop()    
def log():
   root.destroy()
   
a=PhotoImage(file="e.gif")
Label(root,image=a).pack()
Label(root,text='Welcome to BUS TICKETING SYSTEM',relief='raised',font='times 40 bold italic underline',bd=6,bg='white',fg='red').pack()

Label(root,text='We help you plan your journey',relief='raised',font='times 20 bold italic ',bd=0,bg='light grey',fg='black').pack()

Button(root,text='SEARCH BUS',font='times 30 bold',bd=7,bg='dark grey',command=welcome).pack()


Button(root,text="CONTACT",font='times 30 bold',bd=7,bg='dark grey',command=fun).pack(side='left')
Label(root,text='                                    ',relief='raised',font='times 32 bold italic ',bd=0,bg='light grey',fg='black').pack(side='left')
Button(root,text="EXIT",font='times 20 bold',bd=7,bg='dark grey',fg='red',command=log).pack(side='left')
Button(root,text='ADD BUS',font='times 30 bold',bd=7,bg='dark grey',command=images).pack(side='right')





root.mainloop()
