import subprocess
import os
import sys 
import RPi.GPIO as GPIO 
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
ROTATION_COUNT = 3600

def get_picture(camera):
    if camera == 'left':
        subprocess.call(["fswebcam","-r","1920x1080","--no-banner","-d","/dev/video0","/images/image.jpg"])
    elif camera == 'right':
        subprocess.call(["fswebcam","-r","1920x1080","--no-banner","-d","/dev/video1","/images/simage.jpg"])
    f = open("image.jpg","rb")

def rotate_turntable():
    mh = Adafruit_MotorHAT() 
    myStepper.setSpeed(30) 
    myStepper.step(1, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)

def laser(state):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    if state:
        GPIO.output(24, 1)
    else:
        GPIO.output(24, 0)


def main():

    command = sys.argv[0]

    if command == "camera-left":
        get_picture("left")
    elif command == "camera-right":
        get_picture("right")
    elif command == "turntable":
        rotate_turntable()
    elif command == "laser-on":
        laser(True)
    elif command == "laser-off":
        laser(False)
    print(command)

if __name__ == "__main__":
    main()
