from tkinter import *
from tkinter import font
import random

root=Tk()
root.geometry("500x500")
root.config(background="green")
root.title("rps game")

#fonts=list(font.families())
#fonts.sort()
#print(fonts)

ChoiceList=["rock","paper","scissors"]

def PlayGame(PChoice):
    CChoice=random.choice(ChoiceList)
    CChoiceLabel.config(text=CChoice)
    PChoiceLabel.config(text=PChoice)
    if CChoice==PChoice:
        winnerLabel.config(text="Tie")
    elif CChoice=="rock":
        if PChoice=="paper":
            winnerLabel.config(text="Player WINS")
        if PChoice=="scissors":
            winnerLabel.config(text="Computer WINS")
    elif CChoice=="paper":
        if PChoice=="paper":
            winnerLabel.config(text="Player WINS")
        if PChoice=="scissors":
            winnerLabel.config(text="Computer WINS")
    elif CChoice=="scissors":
        if PChoice=="paper":
            winnerLabel.config(text="Player WINS")
        if PChoice=="scissors":
            winnerLabel.config(text="Computer WINS")

headingLabel=Label(root,text="Rock Paper Scissors Game",font=("Arial",25,"bold"),bg="green",fg="black")
headingLabel.pack()
winnerLabel=Label(root,text="Start game",font=("Arial",15),bg="green",fg="black")
winnerLabel.pack()

frame=Frame(root,bg="green")
frame.pack(pady=50)

optionsLabel=Label(frame,text="Pick an option : ",font=("Arial",20),bg="green",fg="black")
optionsLabel.grid(row=0,column=0)
buttonR=Button(frame,text="ROCK",bg="light grey",fg="black",font=("Arial",10,"bold")
               ,command=lambda:PlayGame(ChoiceList[0]))
buttonR.grid(row=0,column=1)
buttonP=Button(frame,text="PAPER",bg="light grey",fg="black",font=("Arial",10,"bold")
               ,command=lambda:PlayGame(ChoiceList[1]))
buttonP.grid(row=0,column=2)
buttonS=Button(frame,text="SCISSORS",bg="light grey",fg="black",font=("Arial",10,"bold")
               ,command=lambda:PlayGame(ChoiceList[2]))
buttonS.grid(row=0,column=3)

frame2=Frame(root,bg="green")
frame2.pack(pady=50)

PChoiceTxtLabel=Label(frame2,text="Player Choice = ",font=("Arial",12,"bold"),bg="green",fg="black")
PChoiceTxtLabel.grid(row=0,column=0)
PChoiceLabel=Label(frame2,text="(---)",font=("Arial",12,"bold"),bg="green",fg="black")
PChoiceLabel.grid(row=0,column=1)
CChoiceTxtLabel=Label(frame2,text="Computer Choice = ",font=("Arial",12,"bold"),bg="green",fg="black")
CChoiceTxtLabel.grid(row=1,column=0)
CChoiceLabel=Label(frame2,text="(---)",font=("Arial",12,"bold"),bg="green",fg="black")
CChoiceLabel.grid(row=1,column=1)

PScoreTxtLabel=Label(frame2,text="Player SCORE = ",font=("Arial",12,"bold"),bg="green",fg="black")
PScoreTxtLabel.grid(row=0,column=2)
PScoreLabel=Label(frame2,text="(---)",font=("Arial",12,"bold"),bg="green",fg="black")
PScoreLabel.grid(row=0,column=3)
CScoreTxtLabel=Label(frame2,text="Computer SCORE = ",font=("Arial",12,"bold"),bg="green",fg="black")
CScoreTxtLabel.grid(row=1,column=2)
CScoreLabel=Label(frame2,text="(---)",font=("Arial",12,"bold"),bg="green",fg="black")
CScoreLabel.grid(row=1,column=3)

root.mainloop()