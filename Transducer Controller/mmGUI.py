from tkinter import *
from movements import moveStepperMM

mmMovements = [
("1 mm", 1),
("2 mm", 2),
("5 mm", 3),
("10 mm", 4),
("25 mm", 5)
("50 mm", 6),
("100 mm", 7),
("250 mm", 8),
("Custom Value", 9),
]

def oneMM():
    moveStepperMM("x", "forward", 1)
def twoMM():
    moveStepperMM("x", "forward", 2)
def fiveMM():
    moveStepperMM("x", "forward", 5)
def tenMM():
    moveStepperMM("x", "forward", 10)
def twentyFiveMM():
    moveStepperMM("x", "forward", 25)
def fiftyMM():
    moveStepperMM("x", "forward", 50)
def hundredMM():
    moveStepperMM("x", "forward", 100)
def twoFiftyMM():
    moveStepperMM("x", "forward", 250)
def customVal():
    moveStepperMM("x", "forward", 1)

options = {1 : oneMM,
           2 : twoMM,
           3 : fiveMM,
           4 : tenMM,
           5 : twentyFiveMM,
           6 : fiftyMM,
           7 : hundredMM,
           8 : twoFiftyMM,
           9 : customVal,
}