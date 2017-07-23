from tkinter import *
#Yo I love indicatoron so what
#More stuff will be added
root = Tk()

v = IntVar()

def manualX():
    choice = "manualX"
    return choice
    root.quit()

def manualY():
    choice = "manualY"
    return choice
    root.quit()

def manualServo():
    choice = "manualServo"
    return choice
    root.quit()

def exit():
    sys.exit()

options = {1 : manualX,
                2 : manualY,
                3 : manualServo,
                0 : exit
}

Movement = [
    ("Manual X-Axis Control", 1),
    ("Manual Y-Axis Control", 2),
    ("Manual Servo Control", 3),
    ("Exit", 0)
]

def ShowChoice():
    choice = options[v.get()]()
    root.quit()
    return choice

def chooseChoice():
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
    choice = ShowChoice()
    return choice