from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
'''root.geometry("500x500")'''
root.title("pizza")

def displaytext():

mainLabel=Label(root,text="Welcome to Pizza Hut")
mainLabel.pack()

frame1=Frame(root)
frame1.pack(pady=(10,0))

selectLabel=Label(frame1,text="Pizza topping - ")
selectLabel.grid(row=0,column=0)

n=IntVar()
toppings=Combobox(frame1,textvariable=n,width=15,state="readonly")
toppings['values']=["Pepperoni","Mushrooms","Margherita","Salad","Olives"]
toppings.current(0)
toppings.grid(row=0,column=1,columnspan=3)

sizeLabel=Label(frame1,text="Size of pizza - ")
sizeLabel.grid(row=1,column=0)

x=IntVar()
sizeOptions1=Radiobutton(frame1,variable=x,text="S",value="small",selectcolor="white")
sizeOptions2=Radiobutton(frame1,variable=x,text="M",value="medium",selectcolor="white")
sizeOptions3=Radiobutton(frame1,variable=x,text="L",value="large",selectcolor="white")
sizeOptions1.grid(row=1,column=1)
sizeOptions2.grid(row=1,column=2)
sizeOptions3.grid(row=1,column=3)

order=Button(root,text="ORDER")
order.pack()

root.mainloop()