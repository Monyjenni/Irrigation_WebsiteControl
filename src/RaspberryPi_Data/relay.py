#turn on or off gpio pin
import RPi.GPIO as GPIO
#delay time between turning on and off the relay
import time
#channel in ras
channel = 20

#board number in raspberry pi
GPIO.setmode(GPIO.BCM)
#relay1
#initialize the pin that used for relay , OUT means output
GPIO.setup(20,GPIO.OUT)

#function to turn motor on based on relay
def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH) # Turn motor on
#function to turn motor off based on relay    
def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH) # Turn motor on
    
if __name__ == '__main__':
    #try to run the code
    try:
        motor_on(channel)
        time.sleep(10)
        motor_off(channel)
        time.sleep(2)
        GPIO.cleanup()
        
    #unless  when hit ctr + c will cleanup the code means to restart  
    except KeyboardInterrupt:    
        GPIO.cleanup()    
        pass    