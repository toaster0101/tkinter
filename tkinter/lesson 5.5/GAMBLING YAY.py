from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.geometry("500x400")
root.config(background="light green")
root.title("slots")
times1=0
times2=0
times3=0
money=10000

def spin():
    global moneyLabel,money
    if money==0:
         messagebox.showinfo("£0 :(","You're broke")
         root.destroy()
    money-=1000
    moneyLabel.config(text="£"+str(money))
    def slot1():
        global times1
        slot1entry.config(bg="white")
        times1=random.randint(7,9)
        slot1entry.config(state=NORMAL)
        def repeater():
            global slot1entry,times1
            slot1entry.delete(0,END)
            slot1entry.insert(0,random.randint(0,9))
            times1-=1
            if times1==0:
                 slot1entry.config(disabledbackground="gold")
                 slot1entry.config(state=DISABLED)
            if times1!=0:
                root.after(250,repeater)
        repeater()
    def slot2():
            global times2
            slot2entry.config(bg="white")
            times2=random.randint(11,13)
            slot2entry.config(state=NORMAL)
            def repeater():
                global slot2entry,times2
                slot2entry.delete(0,END)
                slot2entry.insert(0,random.randint(0,9))
                times2-=1
                if times2==0:
                    slot2entry.config(disabledbackground="gold")
                    slot2entry.config(state=DISABLED)
                if times2!=0:
                    root.after(250,repeater)
            repeater()
    def slot3():
            global times3
            slot3entry.config(bg="white")
            times3=random.randint(15,17)
            slot3entry.config(state=NORMAL)
            def repeater():
                global slot3entry,times3,slot1entry,slot2entry,money,moneyLabel
                slot3entry.delete(0,END)
                slot3entry.insert(0,random.randint(0,9))
                times3-=1
                if times3==0:
                    slot3entry.config(disabledbackground="gold")
                    slot3entry.config(state=DISABLED)
                    if slot1entry.get()==slot2entry.get() and slot1entry.get()==slot3entry.get():
                        jackpotlabel.config(text="JACKPOT")
                        money+=20000
                        moneyLabel.config(text="£"+str(money))
                    elif slot1entry.get()==slot2entry.get() or slot1entry.get()==slot3entry.get() or slot2entry.get()==slot3entry.get():
                        jackpotlabel.config(text="DOUBLE")
                        money+=5000
                        moneyLabel.config(text="£"+str(money))
                    else:
                        jackpotlabel.config(text=":(")
                if times3!=0:
                    root.after(250,repeater)
            repeater()
    slot1()
    slot2()
    slot3()

frame1=Frame(root,bg="red",height=500,width=200)
frame1.place(x=150,y=0)
frame2=Frame(root,bg="dark red",height=100,width=250)
frame2.place(x=125,y=0)
frame3=Frame(root,bg="dark red",height=100,width=250)
frame3.place(x=125,y=300)

slot1entry=Entry(root,bg="white",textvariable="",font=("Arial",40),width=1,state=DISABLED)
slot1entry.place(x=180,y=150)
slot2entry=Entry(root,bg="white",textvariable="",font=("Arial",40),width=1,state=DISABLED)
slot2entry.place(x=230,y=150)
slot3entry=Entry(root,bg="white",textvariable="",font=("Arial",40),width=1,state=DISABLED)
slot3entry.place(x=280,y=150)
jackpotlabel=Label(root,bg="red",text="",font=("Arial",20,"bold"))
jackpotlabel.place(x=0,y=0)
moneyLabel=Label(root,bg="white",text="£"+str(money),font=("Arial",20,"bold"))
moneyLabel.place(x=0,y=38)

spinButton=Button(root,bg="light grey",text="S|1\nP|0\nI|0\nN|0",font=("Consolas",19,"bold"),command=spin)
spinButton.place(x=350,y=130)

root.mainloop()