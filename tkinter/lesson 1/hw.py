from tkinter import *

root=Tk()
root.geometry("500x510")
root.config(background="grey")
root.title("Login")

loginLabel=Label(root,bg="grey",fg="black",text="Login",font=("Arial",30,"bold"))
loginLabel.grid(row=0,column=0,padx=175,pady=20)
userNLabel=Label(root,bg="red",fg="white",text="Username : ",font=("Arial",20))
userNLabel.grid(row=1,column=0,sticky="w",padx=20,pady=10)
userPLabel=Label(root,bg="red",fg="white",text="Password : ",font=("Arial",20))
userPLabel.grid(row=2,column=0,sticky="w",padx=20,pady=60)

nameBox=Entry(root,font=("Arial",15),width="20")
nameBox.grid(row=1,column=0,sticky="w",padx=200)
passWBox=Entry(root,font=("Arial",15),width="20")
passWBox.grid(row=2,column=0,sticky="w",padx=200,pady=60)

root.mainloop()