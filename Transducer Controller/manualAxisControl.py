from actionSelector import choice
#EVERYTHING THAT ACTUALLY WORKS IS COMMENTED OUT BECAUSE I AM PROGRAMMING IT IN ON A WINDOWS BUT IT CAN ONLY RUN ON A RPi
from tkinter import *
#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
from Variables import stepsPerRotation, xPins, stepDegrees, microsteps, yPins

#mh = Adafruit_MotorHAT()

root = Tk()

v = IntVar()
v.set(1)
degreesMoved = 0
microstepsBack = 0

#def turnOffMotors():
    #mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    #mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    #mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    #mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    #print (degreesMoved)

#atexit.register(turnOffMotors)

#myStepperX = mh.getStepper(stepsPerRotation, xPins)
#myStepperY = mh.getStepper(stepsPerRotation, yPins)

languages = [
("1/8 Microstep / 0.225 Degrees", 1),
("1 Step / 1.8 Degrees", 2),
("45 Degrees", 3),
("90 Degrees", 4),
("180 Degrees", 5),
("360 Degrees", 6),
("Reset to Rail", 7),
("Custom Value in Degrees", 8)
]

if choice == "manualX":
    def one_eight():
        global degreesMoved
        degreesMoved = degreesMoved + 0.225
        #myStepperX.step(((1/8)*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("One Eight")
 
    def oneStep():
        global degreesMoved 
        degreesMoved = degreesMoved + 1.8
        #myStepperX.step((1*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("One step")
 
    def fortyFiveDegrees():
        global degreesMoved 
        degreesMoved = degreesMoved + 45
        #myStepperX.step((25*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("45")

    def ninetyDegrees():
        global degreesMoved
        degreesMoved = degreesMoved + 90
        #myStepperX.step((50*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("90") 

    def hundredEightyDegrees():
        global degreesMoved 
        degreesMoved = degreesMoved + 180
        #myStepperX.step((100*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("180")

    def threeHundredSixtyDegrees():
        global degreesMoved 
        degreesMoved = degreesMoved + 360
        #myStepperX.step((200*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("360")

    def reset():    
        global degreesMoved 
        global microstepsBack
        microstepsBack = (microsteps*(degreesMoved/stepDegrees))
        #myStepperX.step(microstepsBack, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("Reset")

    def customVal():
        from customValue import customAmt
        global degreesMoved
        degreesMoved = degreesMoved + customAmt
        customMicrosteps = 8*(customAmt/stepDegrees)
        #myStepperX.step(customAmt, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

    options = {1 : one_eight,
                2 : oneStep,
                3 : fortyFiveDegrees,
                4 : ninetyDegrees,
                5 : hundredEightyDegrees,
                6 : threeHundredSixtyDegrees,
                7 : reset,
                8 : customVal 
    }

    def ShowChoice():
        options[v.get()]()


    Label(root, 
      text="""Select X Axis Movement:""",
      justify = LEFT,
      padx = 20).pack()

    for txt, val in languages:
        Radiobutton(root, 
                    text=txt,
                    indicatoron = 0,
                    width = 20,
                    padx = 20, 
                    variable=v, 
                    command=ShowChoice,
                    value=val).pack(anchor=W)

    mainloop()
    print (degreesMoved)
elif choice == "manualY":
    def one_eight():
        global degreesMoved
        degreesMoved = degreesMoved + 0.225
        #myStepperY.step(((1/8)*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("One Eight")
 
    def oneStep():
        global degreesMoved 
        degreesMoved = degreesMoved + 1.8
        #myStepperY.step((1*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("One step")
 
    def fortyFiveDegrees():
        global degreesMoved 
        degreesMoved = degreesMoved + 45
        #myStepperY.step((25*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("45")

    def ninetyDegrees():
        global degreesMoved
        degreesMoved = degreesMoved + 90
        #myStepperY.step((50*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("90") 

    def hundredEightyDegrees():
        global degreesMoved 
        degreesMoved = degreesMoved + 180
        #myStepperY.step((100*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("180")

    def threeHundredSixtyDegrees():
        global degreesMoved 
        degreesMoved = degreesMoved + 360
        #myStepperY.step((200*8), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("360")

    def reset():    
        global degreesMoved 
        global microstepsBack
        microstepsBack = (microsteps*(degreesMoved/stepDegrees))
        #myStepperY.step(microstepsBack, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
        print ("Reset")

    def customVal():
        from customValue import customAmt
        global degreesMoved
        degreesMoved = degreesMoved + customAmt
        customMicrosteps = 8*(customAmt/stepDegrees)
        #myStepperX.step(customAmt, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

    options = {1 : one_eight,
                2 : oneStep,
                3 : fortyFiveDegrees,
                4 : ninetyDegrees,
                5 : hundredEightyDegrees,
                6 : threeHundredSixtyDegrees,
                7 : reset,
                8 : customVal 
    }

    def ShowChoice():
        options[v.get()]()


    Label(root, 
      text="""Select X Axis Movement:""",
      justify = LEFT,
      padx = 20).pack()

    for txt, val in languages:
        Radiobutton(root, 
                    text=txt,
                    indicatoron = 0,
                    width = 20,
                    padx = 20, 
                    variable=v, 
                    command=ShowChoice,
                    value=val).pack(anchor=W)

    mainloop()
    print (degreesMoved)
else:
    print("error")