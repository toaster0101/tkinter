from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
'''root.geometry("250x250")'''
root.config(background="light green")
root.title("Times Tables")

def table():
    number=n.get()
    length=x.get()
    mTable=""
    for i in range(length):
        mTable+=str(number)+"x"+str(i+1)+" = "+str(number*(i+1))+"\n"
    tablelabel.config(text=mTable)

headingLabel=Label(root,bg="light green",text="Mathematical Tables",font=("Consolas",15,"bold"))
headingLabel.pack()

frame1=Frame(root,bg="light green")
frame1.pack(pady=30)

trLabel=Label(frame1,bg="light green",text="Table And Range",font=("Consolas",12,"bold"))
trLabel.grid(row=0,column=0,columnspan=2)

n=IntVar()
dropbox=Combobox(frame1,textvariable=n,width=4)
dropbox['values']=list(range(1,101))
dropbox.grid(row=1,column=0,sticky=W)

x=IntVar()
button1=Radiobutton(frame1,variable=x,text="10",value=10,bg="light green",selectcolor="white")
button2=Radiobutton(frame1,variable=x,text="20",value=20,bg="light green",selectcolor="white")
button3=Radiobutton(frame1,variable=x,text="30",value=30,bg="light green",selectcolor="white")
button1.grid(row=0,column=3)
button2.grid(row=1,column=3)
button3.grid(row=2,column=3)

regbutton=Button(frame1,bg="green",text="Create",font=("Consolas",8,"bold"),command=table)
regbutton.grid(row=1,column=1)

tablelabel=Label(root,bg="light green",text="",font=("Consolas",8,"bold"))
tablelabel.pack(pady=10)

root.mainloop()