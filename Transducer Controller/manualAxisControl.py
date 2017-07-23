from Variables import xStepPin, xDirPin, yStepPin, yDirPin, stepsPerRotation, stepDegrees, cw, ccw, delay
from actionSelector import chooseChoice
choice = chooseChoice()
from selectDegreeInchesMM import createOptionMovementType
import sys
from time import sleep
#import RPi.GPIO as GPIO

#Pin initiliasition
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(xDirPin, GPIO.OUT)
#GPIO.setup(xStepPin, GPIO.OUT)
#GPIO.setup(yDirPin, GPIO.OUT) 
#GPIO.setup(yStepPin, GPIO.OUT)

if choice == "manualX":
    movementType = createOptionMovementType()
    if movementType == "inches":
        print("a")
    elif movementType == "degrees":
        print("c")
    elif movementType == "mm":
        print("a")
    else:
        sys.exit()
elif choice == "manualY":
    movementType = createOptionMovementType()
    if movementType == "inches":
        print("a")
    elif movementType == "degrees":
        print("c")
    elif movementType == "mm":
        print("d")
    else:
        sys.exit()
else:
    sys.exit()