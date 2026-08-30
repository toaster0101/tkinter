from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x225")
root.config(background="light grey")
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

def apply():
    try:
        currentSelect=box.curselection()
        currentSelect=box.get(currentSelect)
        root.config(bg=currentSelect)
    except TclError:
        messagebox.showinfo("Not A Colour","The colour you are trying to apply is not a colour")

addENT=Entry(root,width=14,bg="light grey")
addENT.pack(pady=(10,0))
addbutton=Button(root,bg="light grey",text="ADD",command=add)
addbutton.pack()
deletebutton=Button(root,bg="light grey",text="DELETE",command=delete)
deletebutton.pack()
applybutton=Button(root,bg="light grey",text="APPLY",command=apply)
applybutton.pack()
clearbutton=Button(root,bg="light grey",text="CLEAR",command=clear)
clearbutton.pack()

box=Listbox(root,width=20,height=10)
box.pack(pady=20)
box.insert(END,"red")
box.insert(END,"blue")
box.insert(END,"yellow")
box.insert(END,"purple")
box.insert(END,"black")

root.mainloop()