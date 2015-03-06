# 09_proximity.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# This project uses the Capsense technique modelled on this:
# http://playground.arduino.cc/Main/CapacitiveSensor
# pin a is the send pin, pin b is the sense pin
a_pin = 18
b_pin = 23
led_pin = 24

threshold = 0

# setup the pin modes
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# return the time taken for the sense pin to flip state as a result of
# the capcitatve effect of being near the sense pin 
def step():
    GPIO.output(a_pin, False)
    t1 = time.time()
    while GPIO.input(b_pin):
        pass
    t2 = time.time()
    time.sleep(0.1)
    GPIO.output(a_pin, True)
    time.sleep(0.1)
    return (t2 - t1) * 1000000

# This function takes 10 readings and finds the largest and puts it in the
# variable - threshold
def calibrate():
    global threshold
    print("Wait! Calibrating")
    n = 10
    maximum = 0
    for i in range(1, n):
        reading = step()
        if reading > maximum:
            maximum = reading
    threshold = maximum * 1.15
    print(threshold)
    print("Calibration Complete")
    
    
calibrate()

try:
    while True:
        reading = step() # take a reading
        GPIO.output(led_pin, (reading > threshold)) # LED on if reading > threshold, otherwise off

finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.