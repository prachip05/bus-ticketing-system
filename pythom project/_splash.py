from tkinter import*
import subprocess
def splash():
    root.destroy()
    fun()
def fun():
    subprocess.call('python pro.py')


root=Tk()
root.title("Prachi Pandey")
root.config(bg='grey')
root.geometry('880x480')
Label(root,text="Welcome",font="times 20 roman bold").grid()


lb=Label(root,text="Name:\tPrachi Pandey\nEnroll:\t191b187\nProject:\tBus Ticketing System",bd=5,font="times 40 roman italic",bg='light grey',fg="black",pady=100,padx=100)
lb.grid(column=0,sticky=E)
root.after(4000,splash)
root.mainloop()
