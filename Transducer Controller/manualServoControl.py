from Variables import servoControlPin
from tkinter import *
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
    #pwm.ChangeDutyCycle(5)
    print ('0')
        
def full():
    #pwm.ChangeDutyCycle(10)
    print ('100')

def halfway():
    #pwm.ChangeDutyCycle(7.5)
    print ('50')

def customMM():
    from customMillimeter import dutyCycleCalc
    #pwn.ChangeDutyCycle(dutyCycleCalc)
    print (dutyCycleCalc)

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
    ("Custom Value (mm)", 4),
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