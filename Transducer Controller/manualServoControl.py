from Variables import servoControlPin
from tkinter import *
from movements import *
import sys
#import RPi.GPIO as GPIO
import time

#Some tuning would be required

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoControlPin, GPIO.OUT)
#pwm = GPIO.PWM(servoControlPin, 50)
#pwm.start(5)

root = Tk()

v = IntVar()

def none():
    setServoMM(0)
    print ('0')
        
def full():
    setServoMM(100)
    print ('100')

def halfway():
    setServoMM(50)
    print ('50')

def customMM():
    from customMillimeter import customAmtMM
    print (customAmtMM)

def exitAll():
    sys.exit()

options = {1 : none,
                2 : halfway,
                3 : full,
                4 : customMM,
                5 : exitAll
}

Movement = [
    ("All the way in (0 mm)", 1),
    ("Halfway (50 mm)", 2),
    ("All the way out (100 mm)", 3),
    ("Custom Value (mm) Click again after entering", 4),
    ("Exit", 5)
]

def ShowChoice():
    options[v.get()]()


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