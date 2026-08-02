from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("250x175")
root.config(background="light grey")
root.title("countdown")
totalseconds=0

def strtCount():
    global totalseconds,hrVar,mnVar,scVar

    hrEntry.config(state=DISABLED)
    mnEntry.config(state=DISABLED)
    scEntry.config(state=DISABLED)
    countdownButton.config(state=DISABLED)

    totalseconds=((int(hrEntry.get())*3600)+(int(mnEntry.get())*60)+int(scEntry.get()))
    print(totalseconds)

    def repeater():
        global totalseconds,hrVar,mnVar,scVar
        mins,seconds=divmod(totalseconds,60)
        hours,mins=divmod(mins,60)
        hrVar.set(f"{hours:02d}")
        mnVar.set(f"{mins:02d}")
        scVar.set(f"{seconds:02d}")
        totalseconds-=1
        if totalseconds==0:
            messagebox.showinfo("TIMES UP","Your countdown has ended.")
            hrEntry.config(state=NORMAL)
            mnEntry.config(state=NORMAL)
            scEntry.config(state=NORMAL)
            countdownButton.config(state=NORMAL)
        else:
            root.after(1000,repeater)
    repeater()

hrVar=StringVar()
hrVar.set("00")
mnVar=StringVar()
mnVar.set("00")
scVar=StringVar()
scVar.set("00")

frame1=Frame(root,bg="light grey")
frame1.pack(pady=20)

hrEntry=Entry(frame1,width=3,textvariable=hrVar,font=("Arial",20,"bold"))
hrEntry.grid(row=0,column=0)
mnEntry=Entry(frame1,width=3,textvariable=mnVar,font=("Arial",20,"bold"))
mnEntry.grid(row=0,column=1,padx=20)
scEntry=Entry(frame1,width=3,textvariable=scVar,font=("Arial",20,"bold"))
scEntry.grid(row=0,column=2)

countdownButton=Button(root,text="Set Countdown",bg="light grey",font=("Arial",15),command=strtCount)
countdownButton.pack(pady=20)

root.mainloop()