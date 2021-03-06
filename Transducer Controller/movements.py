from Variables import *
import sys
from time import sleep

def foo():
    pass

def thatWeirdSquarePattern():
    print("s")
    setServoMM(10)
    for x in range(5):
        forwardSquareSpiral()
        setServoMM(x+11)
        backwordSquareSpiral()
        print(x+11)

def forwardSquareSpiral():
    print('d')
    for x in range(10):
        for x in range(10):
            moveStepperInch("x", "forward", .1)
            sleep(timeRequiredForTransducerToScan)
        moveStepperInch("y", "backward", .1)
        for x in range(10):
            moveStepperInch("x", "backward", .1)
            sleep(timeRequiredForTransducerToScan)
        moveStepperInch("y", "backward", .1)
    print (124)

def backwordSquareSpiral():
    for x in range(10):
        for x in range(10):
            moveStepperInch("x", "backward", .1)
            sleep(timeRequiredForTransducerToScan)
        moveStepperInch("y", "forward", .1)
        for x in range(10):
            moveStepperInch("x", "forward", .1)
            sleep(timeRequiredForTransducerToScan)
        moveStepperInch("y", "forward", .1)

def moveStepperInch(axis, dir, amount):
    # 1 inch = 268.5 revolutions = 53700 steps
    #import RPi.GPIO as GPIO

    #Pin initiliasition
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(xDirPin, GPIO.OUT)
    #GPIO.setup(xStepPin, GPIO.OUT)
    #GPIO.setup(yDirPin, GPIO.OUT) 
    #GPIO.setup(yStepPin, GPIO.OUT)
    amount = 5370 * amount
    amount = int(round(amount))
    if axis == "y":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(yDirPin, cw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(yDirPin, ccw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        else:
            sys.exit()
    elif axis == "x":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(xDirPin, cw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(xDirPin, ccw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        else:
            sys.exit()
    else:
        sys.exit()

def moveStepperMM(axis, dir, amount):
    # 1 inch = 268.5 revolutions = 53700 steps
    # 1 inch = 25.4 mm
    #import RPi.GPIO as GPIO

    #Pin initiliasition
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(xDirPin, GPIO.OUT)
    #GPIO.setup(xStepPin, GPIO.OUT)
    #GPIO.setup(yDirPin, GPIO.OUT) 
    #GPIO.setup(yStepPin, GPIO.OUT)
    amount = (5370 * amount)/25.4
    amount = int(round(amount))
    if axis == "y":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(yDirPin, cw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(yDirPin, ccw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        else:
            sys.exit()
    elif axis == "x":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(xDirPin, cw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(xDirPin, ccw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        else:
            sys.exit()
    else:
        sys.exit()

def moveStepperDegrees(axis, dir, amount):
    # 1 step = 1.8 degrees/ 26.85 = 0.0670391061 degrees per step
    #import RPi.GPIO as GPIO

    #Pin initiliasition
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(xDirPin, GPIO.OUT)
    #GPIO.setup(xStepPin, GPIO.OUT)
    #GPIO.setup(yDirPin, GPIO.OUT) 
    #GPIO.setup(yStepPin, GPIO.OUT)
    amount = (amount)/(1.8/26.85)
    amount = int(round(amount))
    if axis == "y":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(yDirPin, cw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(yDirPin, ccw)
                #GPIO.output(yStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(yStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        else:
            sys.exit()
    elif axis == "x":
        if dir == "forward":
            for x in range (amount):
                #GPIO.output(xDirPin, cw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        elif dir == "backward":
            for x in range (amount):
                #GPIO.output(xDirPin, ccw)
                #GPIO.output(xStepPin, GPIO.HIGH)
                sleep(delay)
                #GPIO.output(xStepPin, GPIO.LOW)
                sleep(delay)
                #GPIO.cleanup()
                foo()
        else:
            sys.exit()
    else:
        sys.exit()

def setServoMM(amount):
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(servoControlPin, GPIO.OUT)
    #pwm = GPIO.PWM(servoControlPin, 50)
    #pwm.start(5)
    dutyCycleCalc = amount*0.05 + 5
    #pwm.ChangeDutyCycle(dutyCycleCalc)
    #GPIO.cleanup()
