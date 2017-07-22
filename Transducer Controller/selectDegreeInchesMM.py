
from tkinter import *
#Yo I love indicatoron so what
#More stuff will be added
root = Tk()

v = IntVar()

def degrees():
    global movementType
    movementType = "degrees"

def inches():
    global movementType
    movementType = "inches"

def mm():
    global movementType
    movementType = "mm"

options = {1 : degrees,
                2 : inches,
                3 : mm
}

Movement = [
    ("Degrees", 1),
    ("Inches", 2),
    ("Millimeters", 3)
]

def ShowChoice():
    options[v.get()]()
    root.destroy()


Label(root, 
      text="""What type of movement do you want?""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in Movement:
    Radiobutton(root, 
                text=txt,
                indicatoron = 0,
                width = 30,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

mainloop()