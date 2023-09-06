#import libraries
import json
from time import strftime
import time
import RPi.GPIO as GPIO

#Sensor: GPIO 21, Relay 1: GPIO 20
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21,GPIO.IN)
GPIO.setup(20,GPIO.OUT)

readings= []
try:
    while True:
        #if it's wet --> no water --> turn off
        if (GPIO.input(21))==0:
            readings.append({
                'Condition': "Plan is Wet" ,
                'Relay':'OFF',
                'Time':strftime("%d/%m/%y at %I:%M%p")  
            })
    
            print(readings)
            GPIO.output(20,False)
#---------------------------------------------------------------------------------------------
        #else it's dry --> water --> turn on    
        elif (GPIO.input(21))==1:
            readings.append({
                'Condition': "Plan is Dry" ,
                'Relay':'ON',
                'Time':strftime("%d/%m/%y at %I:%M%p")
            })

            print(readings)
            #--------------------------------------------
            GPIO.output(20,True)
            #water for 10 sec then stop
            
            time.sleep(10)
            GPIO.cleanup()
finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()




