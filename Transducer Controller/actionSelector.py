from tkinter import *
#Yo I love indicatoron so what
#More stuff will be added
root = Tk()

v = IntVar()

def manualX():
    global choice
    choice = "manualX"

def manualY():
    global choice
    choice = "manualY"

def manualServo():
    global choice
    choice = "manualServo"

options = {1 : manualX,
                2 : manualY,
                3 : manualServo
}

Movement = [
    ("Manual X-Axis Control", 1),
    ("Manual Y-Axis Control", 2),
    ("Manual Servo Control", 3)
]

def ShowChoice():
    options[v.get()]()
    root.destroy()


Label(root, 
      text="""What do you want to do?""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in Movement:
    Radiobutton(root, 
                text=txt,
                indicatoron = 0,
                width = 20,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

mainloop()