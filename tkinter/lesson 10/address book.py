from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

root=Tk()
root.title("Address book")
editT=None
falg=False

everyDictionary={}

def click(event):
    item=box.curselection()
    itemstr=box.get(item)
    details=everyDictionary[itemstr]
    messagebox.showinfo(everyDictionary[itemstr][0],"Name: "+everyDictionary[itemstr][0]+"\n\nE-mail: "+details[1]+"\nNumber: "+details[2]+"\nAddress: "+details[3]+"\nB-Day: "+details[4])

def apply():
    global editT,falg
    everyDictionary[nameEnt.get()]=(nameEnt.get(),emailEnt.get(),numberEnt.get(),addressEnt.get(),bdayEnt.get())
    if editT!=None:
        box.delete(editT)
        box.insert(editT,nameEnt.get())
        editT=None
    else:
        for i in box.get(0,END):
            if i==nameEnt.get():
                falg=True
                messagebox.showinfo("Bad input","There is already an entry with that name")
    if not falg:
        box.insert(END,nameEnt.get())
    print(everyDictionary)

def delete():
    currentSelect=box.curselection()
    if currentSelect:
        box.delete(currentSelect)

def edit():
    global editT
    item=box.curselection()
    itemstr=box.get(item)
    details=everyDictionary[itemstr]
    nameEnt.delete(0,END)
    nameEnt.insert(0,details[0])
    emailEnt.delete(0,END)
    emailEnt.insert(0,details[1])
    numberEnt.delete(0,END)
    numberEnt.insert(0,details[2])
    addressEnt.delete(0,END)
    addressEnt.insert(0,details[3])
    bdayEnt.delete(0,END)
    bdayEnt.insert(0,details[4])
    editT=item

def save():
    tbsaved=asksaveasfile(defaultextension=".txt")
    print(everyDictionary,file=tbsaved)
    box.delete(0,END)

def open():
    global everyDictionary
    tbopened=askopenfile(title="openfile")
    box.delete(0,END)
    everyDictionary.clear()
    everyDictionary=eval(tbopened.read())
    for i in everyDictionary.keys():
        box.insert(END,i)

frameAdd=Frame(root)
frameAdd.pack(pady=(10,30))

addressText=Label(frameAdd,text="Address book")
addressText.grid(row=0,column=0)
addressOpen=Button(frameAdd,text="OPEN",command=open)
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

delButton=Button(frameMid,text="DELETE",command=delete)
delButton.grid(row=5,column=0,pady=10)
editButton=Button(frameMid,text="EDIT",command=edit)
editButton.grid(row=5,column=1,pady=10)
applyButton=Button(frameMid,text="APPLY",command=apply)
applyButton.grid(row=5,column=3,pady=10)
saveButton=Button(root,text="SAVE",width=15,command=save)
saveButton.pack()

root.mainloop()