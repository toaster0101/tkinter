from tkinter import *

root=Tk()
root.geometry("500x400")
root.config(background="light green")
root.title("slots")

frame1=Frame(root,bg="red",height=500,width=200)
frame1.place(x=150,y=0)
frame2=Frame(root,bg="red",height=100,width=250)
frame2.place(x=125,y=0)
frame3=Frame(root,bg="red",height=100,width=250)
frame3.place(x=125,y=300)

slot1Label=Label(frame1,bg="white",text="2",font=("Arial",40))
slot1Label.grid(side=LEFT)
slot2Label=Label(frame1,bg="white",text="2",font=("Arial",40))
slot2Label.grid(side=LEFT)
slot3Label=Label(frame1,bg="white",text="2",font=("Arial",40))
slot3Label.grid(side=LEFT)

root.mainloop()