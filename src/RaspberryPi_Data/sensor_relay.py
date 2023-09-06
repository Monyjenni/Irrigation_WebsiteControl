#import libraries
from time import strftime
import time
import RPi.GPIO as GPIO

#Sensor: GPIO 21, Relay 1: GPIO 20
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21,GPIO.IN)
GPIO.setup(20,GPIO.OUT)

try:
    while True:
        #if it's wet --> no water --> turn off
        if (GPIO.input(21))==0:
            print ("Plant Is Wet!")
            full_datetime = strftime("%d/%m/%y at %I:%M%p")
            f = open("/home/pi/Desktop/text.txt", "a")
            f.write(" Plant Is Wet!")
            f.write("Relay is OFF",full_datetime)
            print("Relay is OFF at",full_datetime)
            GPIO.output(20,False)
        #else it's dry --> water --> turn on    
        elif (GPIO.input(21))==1:
            f = open("/home/pi/Desktop/text.txt", "a")
            full_datetime = strftime("%d/%m/%y at %I:%M%p")
            f.write("Relay is ON")
            print("The plant is dry :'(")
            print("Relay is ON, Date:",full_datetime)
            GPIO.output(20,True)
            #water for 10 sec then stop
            
            time.sleep(10)
            GPIO.cleanup()
finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()




