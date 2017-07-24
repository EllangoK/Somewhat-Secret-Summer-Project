from tkinter import *
from movements import moveStepperInch

inchMovements = [
("0.25 inches", 1),
("0.5 inches", 2),
("1 inch", 3),
("2 inches", 4),
("Custom Value", 5)
]

def point25():
    moveStepperInch("x", "forward", .25)
def point5():
    moveStepperInch("x", "forward", .5)
def oneInch():
    moveStepperInch("x", "forward", 1)
def twoInch():
    moveStepperInch("x", "forward", 2)
def customVal():
    moveStepperInch("x", "forward", .25)

options = {1 : point25,
           2 : point5,
           3 : oneInch,
           4 : twoInch,
           5 : customVal 
}