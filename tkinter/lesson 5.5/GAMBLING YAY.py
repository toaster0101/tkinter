from tkinter import *
import random

root=Tk()
root.geometry("500x400")
root.config(background="light green")
root.title("slots")

frame1=Frame(root,bg="red",height=500,width=200)
frame1.place(x=150,y=0)
frame2=Frame(root,bg="dark red",height=100,width=250)
frame2.place(x=125,y=0)
frame3=Frame(root,bg="dark red",height=100,width=250)
frame3.place(x=125,y=300)

slot1Label=Label(root,bg="white",text="2",font=("Arial",40))
slot1Label.place(x=180,y=150)
slot2Label=Label(root,bg="white",text="2",font=("Arial",40))
slot2Label.place(x=230,y=150)
slot3Label=Label(root,bg="white",text="2",font=("Arial",40))
slot3Label.place(x=280,y=150)

spinButton=Button(root,bg="light grey",text="S\nP\nI\nN",font=("Arial",19,"bold"))
spinButton.place(x=350,y=130)

root.mainloop()