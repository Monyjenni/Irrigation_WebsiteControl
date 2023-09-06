#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def callback(channel):
    if GPIO.input(channel):
        print ("Water Not Detected!")
        f = open("/home/pi/Desktop/text.txt", "a")
        f.write(" Water not detected")
    else:
        print ("Water Detected!")
        f = open("/home/pi/Desktop/text.txt", "a")
        f.write(" Water detected")
    
    


