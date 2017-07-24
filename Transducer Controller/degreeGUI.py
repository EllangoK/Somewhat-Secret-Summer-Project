from tkinter import *
from movements import moveStepperDegrees

degreeMovements = [
("1.8 inches", 1),
("45 inches", 2),
("90 inch", 3),
("180 inches", 4),
("360 degrees", 5),
("Custom Value", 6)
]

def onePointEight():
    moveStepperDegrees("x", "forward", 1.8)
def fortyFive():
    moveStepperDegrees("x", "forward", 45)
def ninety():
    moveStepperDegrees("x", "forward", 90)
def oneEighty():
    moveStepperDegrees("x", "forward", 180)
def threeSixty():
    moveStepperDegrees("x", "forward", 360)
def customVal():
    moveStepperDegrees("x", "forward", 1.8)

options = {1 : onePointEight,
           2 : fortyFive,
           3 : ninety,
           4 : oneEighty,
           5 : threeSixty,
           6 : customVal
}