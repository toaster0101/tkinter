from tkinter import *
from time import strftime

root=Tk()
root.geometry("400x200")
root.config(background="light blue")
root.title("time")
time12=False


def time_Update():
    timeMode=strftime("%H:%M:%S")
    if time12:
        timeMode=strftime("%I:%M:%S.%p")
    timeLabel.config(text=timeMode)
    dateLabel.config(text=strftime("%d/%b/%Y"))
    timeLabel.after(1000,time_Update)
    dateLabel.after(1000,time_Update)

def HR12():
    global time12
    time12=True

def HR24():
    global time12
    time12=False

timeLabel=Label(root,bg="light blue",fg="black",font=("Arial",30,"bold"))
timeLabel.pack(pady=20)
dateLabel=Label(root,bg="light blue",fg="black",font=("Arial",15,"bold"))
dateLabel.pack()
frame1=Frame(bg="light blue")
frame1.pack(pady=20)
PMbutton=Button(frame1,text="24HR Clock mode",bg="dark green",fg="black",font=("Arial",12,"bold"),command=HR24)
PMbutton.grid(row=0,column=0)
AMbutton=Button(frame1,text="12HR Clock mode",bg="dark green",fg="black",font=("Arial",12,"bold"),command=HR12)
AMbutton.grid(row=0,column=1)
time_Update()

root.mainloop()