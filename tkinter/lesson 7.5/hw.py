from tkinter import *
from tkinter.ttk import Combobox
import calendar

root=Tk()
root.geometry("250x300")
root.title("months")

def showcal():
    month=str(n.get())
    yr=yrEnt.get()
    calcontent=calendar.month(yr,month)
    calLabel.config(text=calcontent)
    calLabel.pack()

frame1=Frame(root)
frame1.pack()

yrlbl=Label(frame1,text="Enter Year: ")
yrlbl.grid(row=0,column=0)
yrEnt=Entry(frame1,width=20)
yrEnt.grid(row=0,column=1)

monthLabel=Label(frame1,text="Select Month: ")
monthLabel.grid(row=1,column=0,pady=10)

n=IntVar()
dropbox=Combobox(frame1,textvariable=n,width=15)
dropbox['values']=list(range(1,13))
dropbox.current(0)
dropbox.grid(row=1,column=1,pady=10)

shwcal=Button(root,text="SHOW CALENDAR",command=showcal)
shwcal.pack()

calLabel=Label(root,text="")

root.mainloop()