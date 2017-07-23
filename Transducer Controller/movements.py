from Variables import *
import sys
from time import sleep
#import RPi.GPIO as GPIO

#Pin initiliasition
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(xDirPin, GPIO.OUT)
#GPIO.setup(xStepPin, GPIO.OUT)
#GPIO.setup(yDirPin, GPIO.OUT) 
#GPIO.setup(yStepPin, GPIO.OUT)

def moveStepperInch(axis, dir, amount):
    # 1 inch = 268.5 revolutions = 53700 steps
    amount = 53700 * amount
    amount = int(amount)
    if axis == "y":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(yDirPin, cw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("l")
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(yDirPin, ccw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("2")
        else:
            sys.exit()
    elif axis == "x":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(xDirPin, cw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("3")
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(xDirPin, ccw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("4")
        else:
            sys.exit()
    else:
        sys.exit()

def moveStepperMM(axis, dir, amount):
    # 1 inch = 268.5 revolutions = 53700 steps
    # 1 inch = 25.4 mm
    amount = (53700 * amount)/25.4
    amount = int(amount)
    if axis == "y":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(yDirPin, cw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("l")
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(yDirPin, ccw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("2")
        else:
            sys.exit()
    elif axis == "x":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(xDirPin, cw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("3")
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(xDirPin, ccw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("4")
        else:
            sys.exit()
    else:
        sys.exit()

def moveStepperDegrees(axis, dir, amount):
    # 1 step = 1.8 degrees/ 26.85 = 0.0670391061 degrees per step
    amount = (amount)/(1.8/26.85)
    amount = int(amount)
    if axis == "y":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(yDirPin, cw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("l")
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(yDirPin, ccw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("2")
        else:
            sys.exit()
    elif axis == "x":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(xDirPin, cw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("3")
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(xDirPin, ccw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                #sleep(delay)
                #GPIO.cleanup()
                print ("4")
        else:
            sys.exit()
    else:
        sys.exit()