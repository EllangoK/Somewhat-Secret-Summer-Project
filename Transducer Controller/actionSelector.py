from tkinter import *
#Yo I love indicatoron so what
#More stuff will be added
root = Tk()

v = IntVar()

#def manualX():
#    choice = "manualX"
#    return choice

#def manualY():
#    choice = "manualY"
#    return choice

#def manualServo():
#    choice = "manualServo"
#    return choice

#options = {1 : manualX,
#                2 : manualY,
#                3 : manualServo
#}

Movement = [
    ("Manual X-Axis Control", 1),
    ("Manual Y-Axis Control", 2),
    ("Manual Servo Control", 3)
]

def ShowChoice():
    #options[v.get()]()
    root.quit()
    if v.get() == 1:
        choice = "manualX"
        return choice
    elif v.get() == 2:
        choice = "manualY"
        return choice
    elif v.get() == 3:
        choice = "manualServo"
        return choice
    else:
        sys.exit()
        return choice


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