from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
root.geometry("250x250")
root.config(background="light green")
root.title("Times Tables")

headingLabel=Label(root,bg="light green",text="Mathematical Tables",font=("Consolas",15,"bold"))
headingLabel.pack()
frame1=Frame(root,bg="light green")
frame1.pack(pady=30)
trLabel=Label(frame1,bg="light green",text="Table And Range",font=("Consolas",12,"bold"))
trLabel.grid(row=0,column=0)
n=IntVar()
dropbox=Combobox(frame1,textvariable=n,width=4)
dropbox['values']=list(range(1,101))
dropbox.grid(row=1,column=0)

root.mainloop()