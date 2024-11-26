import RPi.GPIO as GPIO
import time
SPEED_OF_SOUND = 343

TRIG = 26
ECHO = 27
BUTTON = 24  # can change later*

GREEN = 17   #  ^^^
YELLOW1 = 16
YELLOW2 = 13
RED1 = 5 
RED2 = 6


GPIO.setup(BUTTON, GPIO.IN) # button input
GPIO.setup(TRIG, GPIO.OUT)	# TRIG is an output
GPIO.setup(ECHO, GPIO.IN)	# ECHO is an input
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW1, GPIO.OUT)
GPIO.setup(YELLOW2, GPIO.OUT)
GPIO.setup(RED1, GPIO.OUT)
GPIO.setup(RED2, GPIO.OUT)





def getDistance():
    # trigger the sensor by setting it high for a short time and then setting it low
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)

    # wait for the ECHO pin to read high
    # once the ECHO pin is high, the start time is set
    # once the ECHO pin is low again, the end time is set
    while (GPIO.input(ECHO) == GPIO.LOW):
        start = time()
    while (GPIO.input(ECHO) == GPIO.HIGH):
        end = time()

    # calculate the duration that the ECHO pin was high
    # this is how long the pulse took to get from the sensor to the object -- and back again
    duration = end - start
    # calculate the total distance that the pulse traveled by factoring in the speed of sound (m/s)
    distance = duration * SPEED_OF_SOUND
    # the distance from the sensor to the object is half of the total distance traveled
    distance /= 2
    # convert from meters to centimeters
    distance *= 100

    return distance

#def checkLights(dist):
    













def main():
    active = True
    while(active == True):
        
        
    


main()