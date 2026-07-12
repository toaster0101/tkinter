from tkinter import *

root=Tk()
root.geometry("700x400")
root.config(background="light blue")
root.title("Kg-->gram,pound & ounce")

def ConvertFunc():
    try:
        inputKg=float(kgBox.get())
        resultG=str(inputKg*1000)
        resultO=str(inputKg*35.274)
        resultP=str(inputKg*2.205)
        resultGLabel.config(text=resultG)
        resultOLabel.config(text=resultO)
        resultPLabel.config(text=resultP)
        resultGLabel.grid(row=3,column=0,sticky=W,padx=20)
        resultOLabel.grid(row=3,column=1,sticky=W)
        resultPLabel.grid(row=3,column=2)
    except ValueError:
        resultGLabel.config(text="You can only input numbers")
        resultOLabel.config(text="You can only input numbers")
        resultPLabel.config(text="You can only input numbers")
        resultGLabel.grid(row=3,column=0,sticky=W,padx=20)
        resultOLabel.grid(row=3,column=1,sticky=W)
        resultPLabel.grid(row=3,column=2)

kgLabel=Label(root,bg="light blue",fg="white",text="Enter kg:",font=("Ariel",30,"bold"))
kgLabel.grid(row=0,column=0,padx=50,pady=75)
kgBox=Entry(root,font=("Arial",15),width=20)
kgBox.grid(row=0,column=1)
convertButton=Button(root,bg="white",fg="light blue",text="CONVERT",font=("Arial",15,"bold"),command=ConvertFunc)
convertButton.grid(row=0,column=2,padx=50)

gramLabel=Label(root,bg="light blue",fg="white",text="Grams:",font=("Ariel",30,"bold"))
gramLabel.grid(row=1,column=0,sticky=W,padx=20)
ounceLabel=Label(root,bg="light blue",fg="white",text="Ounces:",font=("Ariel",30,"bold"))
ounceLabel.grid(row=1,column=1,sticky=W)
poundLabel=Label(root,bg="light blue",fg="white",text="Pounds:",font=("Ariel",30,"bold"))
poundLabel.grid(row=1,column=2)

resultGLabel=Label(root,bg="light blue",fg="white",text="Pounds:",font=("Ariel",10,"bold"))
resultOLabel=Label(root,bg="light blue",fg="white",text="Pounds:",font=("Ariel",10,"bold"))
resultPLabel=Label(root,bg="light blue",fg="white",text="Pounds:",font=("Ariel",10,"bold"))

root.mainloop()