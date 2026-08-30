from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.config(background="light grey")
root.title("tic tac toe")
Multi=False
x=1

def clicked(r,c):
    global x,Multi,board
    if Multi:
        if x%2!=0 and board[r][c]["text"]=="":
            board[r][c]["text"]="X"
            winCheck()
        elif board[r][c]["text"]=="":
            board[r][c]["text"]="O"
            winCheck()
        x+=1
    else:
        list1=[]
        if board[r][c]["text"]=="":
            board[r][c]["text"]="X"
            winCheck()
        for i in range(3):
            for j in range(3):
                if board[i][j]["text"]=="":
                    list1.append((i,j))
        if list1:
            choice=random.choice(list1)
            board[choice[0]][choice[1]]["text"]="O"
            winCheck()

def winCheck():
    for i in range(3):
        if board[i][0]["text"]==board[i][1]["text"]==board[i][2]["text"]!="":
            messagebox.showinfo("Win",(board[i][0]["text"])+" Has Won")
            restart()
    for j in range(3):
        if board[0][j]["text"]==board[1][j]["text"]==board[2][j]["text"]!="":
            messagebox.showinfo("Win",(board[0][j]["text"])+" Has Won")
            restart()

def restart():
    for i in range(3):
        for j in range(3):
            board[i][j]["text"]=""

def multiplayer():
    global Multi
    Multi=True

def singleplayer():
    global Multi
    Multi=False

frame1=Frame(root,bg="light grey")
frame1.pack()

board=[[None for i in range(3)]for j in range(3)]
for i in range(3):
    for j in range(3):
        board[i][j]=Button(frame1,width=5,height=2,command=lambda r=i,c=j:clicked(r,c))
        board[i][j].grid(row=i,column=j)

singleP=Button(root,text="SinglePlayer",command=singleplayer)
singleP.pack(side=LEFT)
MultiP=Button(root,text="MultiPlayer",command=multiplayer)
MultiP.pack(side=RIGHT)
resetB=Button(root,text="Reset",command=restart)
resetB.pack()

root.mainloop()