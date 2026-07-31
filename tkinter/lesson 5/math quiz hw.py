from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.geometry("500x500")
root.config(background="light green")
root.title("math quiz")
score=0
q1Flag=False
q2Flag=False
q3Flag=False
q1val1=str(random.randint(11,46))
q1val2=str(random.randint(11,46))
q2val1=str(random.randint(1,4)*10)
q2val2=str(random.randint(1,4)*10)
q3val1=str(random.randint(1,3)*10)
q3val2=str(random.randint(1,3)*10)
message=""

def strt():
    messagebox.showinfo("Q1","What is "+q1val1+" PLUS "+q1val2+("?"))
    q1entry.config(state=NORMAL)
    q1guessButton.config(state=NORMAL)

def q2Strt():
    global q1Flag,score
    messagebox.showinfo("Q2","What is "+q2val1+" TIMES "+q2val2+("?"))
    q2entry.config(state=NORMAL)
    q2guessButton.config(state=NORMAL)
    if not q1Flag:
        if float(q1entry.get())==(float(q1val1)+float(q1val2)):
            score+=1
            q1Flag=True


def q3Strt():
    global q2Flag,score
    messagebox.showinfo("Q3","What is "+q3val1+" DIVIDED BY "+q3val2+("?"))
    q3entry.config(state=NORMAL)
    q3guessButton.config(state=NORMAL)
    if not q2Flag:
            if float(q2entry.get())==(float(q2val1)*float(q2val2)):
                score+=1
                q2Flag=True

def endScore():
    global message,q3Flag,score
    if not q3Flag:
        if float(q3entry.get())==(float(q3val1)/float(q3val2)):
            score+=1
            q3Flag=True
    if score==0:
        message="You got none right :("
    elif score==1:
        message="Only 1 right :("
    elif score==2:
        message="Almost perfect 2/3 :)"
    else:
        message="PERFECT 3/3"
    messagebox.showinfo("SCORE",message)

mainLabel=Label(root,text="Welcome to The",font=("Arial",20),fg="black",bg="light green")
mainLabel.pack(pady=(30,0))
mainLabel=Label(root,text="MATH QUIZ",font=("Arial",30,"bold"),fg="black",bg="light green")
mainLabel.pack()
startButton=Button(root,bg="grey",text="  Start  ",font=("Arial",20,"bold"),fg="black",command=strt)
startButton.pack(pady=20)

answFrame=Frame(root,bg="light green")
answFrame.pack(pady=30)

q1Label=Label(answFrame,text="Q1 Answer:",font=("Arial",15,"bold"),fg="black",bg="light green")
q1Label.grid(row=0,column=0)
q1entry=Entry(answFrame,font=("Arial",15,"bold"),state=DISABLED)
q1entry.grid(row=0,column=1)
q1guessButton=Button(answFrame,text="GUESS",bg="light grey",fg="black",font=("Arial",12,"bold"),state=DISABLED,command=q2Strt)
q1guessButton.grid(row=0,column=2,padx=5)

q2Label=Label(answFrame,text="Q2 Answer:",font=("Arial",15,"bold"),fg="black",bg="light green")
q2Label.grid(row=1,column=0,pady=20)
q2entry=Entry(answFrame,font=("Arial",15,"bold"),state=DISABLED)
q2entry.grid(row=1,column=1,pady=20)
q2guessButton=Button(answFrame,text="GUESS",bg="light grey",fg="black",font=("Arial",12,"bold"),state=DISABLED,command=q3Strt)
q2guessButton.grid(row=1,column=2,padx=5)

q3Label=Label(answFrame,text="Q3 Answer:",font=("Arial",15,"bold"),fg="black",bg="light green")
q3Label.grid(row=2,column=0)
q3entry=Entry(answFrame,font=("Arial",15,"bold"),state=DISABLED)
q3entry.grid(row=2,column=1)
q3guessButton=Button(answFrame,text="GUESS",bg="light grey",fg="black",font=("Arial",12,"bold"),state=DISABLED,command=endScore)
q3guessButton.grid(row=2,column=2,padx=5)

root.mainloop()