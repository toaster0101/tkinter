from tkinter import *
import random

root=Tk()
root.geometry("300x200")
root.config(background="green")
root.title("template")

def randomC():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    root.config(background=f"#{r:02x}{g:02x}{b:02x}")

button1=Button(root,bg="black",fg="white",text="color randomizer",command=randomC)
button1.pack(pady=10)

root.mainloop()