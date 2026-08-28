from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.geometry("500x300")
root.config(bg="grey")
root.title("template")

def clear():
    box.delete(0,END)

def add():
    box.insert(END,addENT.get())
    addENT.delete(0,END)

def delete():
    currentSelect=box.curselection()
    if currentSelect:
        box.delete(currentSelect)

def save():
    fout=asksaveasfile(defaultextension=".txt")
    for i in box.get(0,END):
        print(i,file=fout)
    box.delete(0,END)

def load():
    fin=askopenfile(title="Open File")
    box.delete(0,END)
    item=fin.readlines()
    for i in item:
        box.insert(END,i)

loadButton=Button(root,text="LOAD",width=7,font=("Arial",10,"bold"),bg="light grey",command=load)
loadButton.pack(pady=125,side=RIGHT)
saveButton=Button(root,text="SAVE",width=7,font=("Arial",10,"bold"),bg="light grey",command=save)
saveButton.pack(pady=125,side=LEFT)
deleteButton=Button(root,text="DELETE",width=7,font=("Arial",10,"bold"),bg="light grey",command=delete)
deleteButton.pack(pady=10)
addENT=Entry(root,width=12,font=("Arial",12),bg="light grey")
addENT.pack()
addButton=Button(root,text="ADD",width=7,font=("Arial",10,"bold"),bg="light grey",command=add)
addButton.pack()
clearButton=Button(root,text="CLEAR",width=7,font=("Arial",10,"bold"),bg="light grey",command=clear)
clearButton.pack(pady=10)

box=Listbox(root,width=40,height=15)
box.pack(pady=20)
for i in range(100):
    box.insert(END,"LIST"+str(i))

root.mainloop()