from tkinter import *
import random

root=Tk()
root.geometry("500x500")
root.config(background="green")
root.title("hw")
colourList=["red","blue","green","light green","light blue","grey","purple"]

def colourChange():
    colourRNG=random.choice(colourList)
    root.config(background=colourRNG)
    textLabel.config(bg=colourRNG)
    colourRNG2=random.choice(colourList)
    while colourRNG2==colourRNG:
        colourRNG2=random.choice(colourList)
    textLabel.config(fg=colourRNG2)
    textLabel.after(1000,colourChange)
    root.after(1000,colourChange)

textLabel=Label(root,text="text",font=("Arial",20,"bold"))
textLabel.pack()
colourChange()

root.mainloop()