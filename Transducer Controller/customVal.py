from tkinter import *
import sys

root = Tk()

def customVal(str):
    def getCustomAmt():
        global customAmt
        customAmt = int(E1.get())
        root.destroy()       
    submit = Button(root, text ="Submit", command = getCustomAmt)
    if str == "inch":
        label1 = Label( root, text="Custom Value in Inches")
        E1 = Entry(root, bd =5)

        label1.pack()
        E1.pack()
        submit.pack(side =BOTTOM) 
        root.mainloop()
        return customAmt
    elif str == "mm":
        label1 = Label( root, text="Custom Value in Millimeters")
        E1 = Entry(root, bd =5)

        label1.pack()
        E1.pack()
        submit.pack(side =BOTTOM) 
        root.mainloop()
        return customAmt
    elif str == "degree":
        label1 = Label( root, text="Custom Value in Degrees")
        E1 = Entry(root, bd =5)

        label1.pack()
        E1.pack()
        submit.pack(side =BOTTOM) 
        root.mainloop()
        return customAmt
    else:
        sys.exit()
