from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.geometry("500x500")
root.config(background="light green")
root.title("gtn")
number=random.randint(0,100)
triesnum=0

def startGuess():
    guessButton.config(state=NORMAL)
    nameButton.config(state=DISABLED)
    guessInput.config(state=NORMAL)
    nameInput.config(state=DISABLED)
    messagebox.showinfo("WELCOME",
                        "Hello "+nameInput.get()+", And Welcome TO GEUSS THE NUMBER!\n You must guess the number I "
                        "am thinking of, it is from 0-100")

def guess():
    global triesnum
    message=""
    if int(guessInput.get())>number:
        message="too high"
        triesnum+=1
    elif int(guessInput.get())<number:
        message="too low"
        triesnum+=1
    else:
        message="CORRECT!!!"
        guessInput.config(state=DISABLED)
        guessButton.config(state=DISABLED)
        tries=Label(root,text="Congratulations!, You took "+str(triesnum)+" tries",
                    font=("Arial",20,"bold"),fg="black",bg="light green")
        tries.pack()
    messagebox.showinfo("Guess info","Your guess is "+message)

mainLabel=Label(root,text="Welcome to\nGTN",font=("Arial",20,"bold"),fg="black",bg="light green")
mainLabel.pack(pady=30)

frame1=Frame(root,bg="light green")
frame1.pack()

nameInputLabel=Label(frame1,bg="light green",text="Enter your name :",fg="black",font=("Arial",15,"bold"))
nameInputLabel.grid(row=0,column=0)
nameInput=Entry(frame1,font=("Arial",15),state=NORMAL)
nameInput.grid(row=1,column=0)
nameButton=Button(frame1,text="NEXT",bg="light grey",fg="black",font=("Arial",15,"bold"),state=NORMAL,command=startGuess)
nameButton.grid(row=1,column=1,padx=20)

nameInputLabel=Label(frame1,bg="light green",text="Enter your Guess :",fg="black",font=("Arial",15,"bold"))
nameInputLabel.grid(row=2,column=0,pady=(20,0))
guessInput=Entry(frame1,font=("Arial",15),state=DISABLED)
guessInput.grid(row=3,column=0)
guessButton=Button(frame1,text="GUESS",bg="light grey",fg="black",font=("Arial",15,"bold"),state=DISABLED,command=guess)
guessButton.grid(row=3,column=1,padx=20)

root.mainloop()