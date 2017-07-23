from tkinter import *

root = Tk()

customAmt = 0

label1 = Label( root, text="Custom Millimeter in Degrees")
E1 = Entry(root, bd =5)

def getCustomAmt():
    global customAmtMM
    customAmtMM = int(E1.get())
    root.destroy()

submit = Button(root, text ="Submit", command = getCustomAmt)

label1.pack()
E1.pack()
submit.pack(side =BOTTOM) 
root.mainloop()