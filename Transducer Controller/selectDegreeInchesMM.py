from tkinter import *

master = Tk()

def option_changed(*args):
    variable = StringVar(master)
    variable.set("Degrees") # default value
    variable.trace("w", option_changed)
    master.quit()
    return variable.get()

def createOptionMovementType():
    variable = StringVar(master)
    variable.set("Degrees") # default value
    variable.trace("w", option_changed)
    w = OptionMenu(master, variable, "Degrees", "Inches", "Millimeters")
    w.pack()

    mainloop()
    movementType = option_changed()
    return movementType