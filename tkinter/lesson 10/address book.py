from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("template")

everyDictionary={}

def click(event):
    item=box.curselection()
    itemstr=box.get(item)
    details=everyDictionary[itemstr]
    details2="Name: "+everyDictionary[itemstr]+"\n\n"
    details2+=
    messagebox.showinfo("Entry","E-mail: "+details[0]+"\nNumber: "+details[1]+"\nAddress: "+details[2]+"\nB-Day: "+details[3])

def apply():
    everyDictionary[nameEnt.get()]=(emailEnt.get(),numberEnt.get(),addressEnt.get(),bdayEnt.get())
    box.insert(END,nameEnt.get())

frameAdd=Frame(root)
frameAdd.pack(pady=(10,30))

addressText=Label(frameAdd,text="Address book")
addressText.grid(row=0,column=0)
addressOpen=Button(frameAdd,text="OPEN")
addressOpen.grid(row=0,column=1)

frameMid=Frame(root)
frameMid.pack()

box=Listbox(frameMid,height=12,width=20)
box.grid(row=0,column=0,rowspan=5,columnspan=2)
box.bind('<<ListboxSelect>>',click)
nameText=Label(frameMid,text="Name: ")
nameText.grid(row=0,column=2,padx=(10,0))
emailText=Label(frameMid,text="Email: ")
emailText.grid(row=1,column=2,padx=(10,0))
numberText=Label(frameMid,text="Number: ")
numberText.grid(row=2,column=2,padx=(10,0))
addressText=Label(frameMid,text="Address: ")
addressText.grid(row=3,column=2,padx=(10,0))
bdayText=Label(frameMid,text="B-Day: ")
bdayText.grid(row=4,column=2,padx=(10,0))

nameEnt=Entry(frameMid,width=10)
nameEnt.grid(row=0,column=3)
emailEnt=Entry(frameMid,width=10)
emailEnt.grid(row=1,column=3)
numberEnt=Entry(frameMid,width=10)
numberEnt.grid(row=2,column=3)
addressEnt=Entry(frameMid,width=10)
addressEnt.grid(row=3,column=3)
bdayEnt=Entry(frameMid,width=10)
bdayEnt.grid(row=4,column=3)

delButton=Button(frameMid,text="DELETE")
delButton.grid(row=5,column=0,pady=10)
editButton=Button(frameMid,text="EDIT")
editButton.grid(row=5,column=1,pady=10)
applyButton=Button(frameMid,text="APPLY",command=apply)
applyButton.grid(row=5,column=3,pady=10)
saveButton=Button(root,text="SAVE",width=15)
saveButton.pack()

root.mainloop()