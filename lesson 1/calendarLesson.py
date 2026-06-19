from tkinter import *
import calendar

root=Tk()
root.geometry("500x500")
root.config(background="green")
root.title("Calendar")

def buttonPress():
    calendarWindow=Tk()
    calendarWindow.geometry("600x600")
    calendarWindow.config(background="white")
    calendarWindow.title("Calendar")
    year=int(inputBox.get())
    calendarContent=calendar.calendar(year)
    calendarLabel=Label(calendarWindow,text=calendarContent,font=("Consolas",10),justify=LEFT)
    calendarLabel.grid(row=0,column=0)
    calendarWindow.mainloop()

titleLabel=Label(root,bg="green",fg="black",text="CALENDAR",font=("Arial",30,"bold"))
titleLabel.grid(row=0,column=0,padx=130,pady=20)
yearLabel=Label(root,bg="dark green",fg="black",text="Year : ",font=("Arial",20))
yearLabel.grid(row=1,column=0,sticky="w",padx=20)
inputBox=Entry(root,font=("Arial",15),width="5")
inputBox.grid(row=1,column=0,sticky="w",padx=110)
button=Button(root,bg="red",text="Calendar",fg="black",font=("Arial",15,"bold"),command=buttonPress)
button.grid(row=2,column=0,padx=110,pady=20)

root.mainloop()