# 02_blink_twice.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
red_pin1 = 18
red_pin2 = 23

GPIO.setup(red_pin1, GPIO.OUT)
GPIO.setup(red_pin2, GPIO.OUT)
        
try:
    while True:
        GPIO.output(red_pin1, True)     # True means that LED turns on
        GPIO.output(red_pin2, False)    # False means that LED turns off
        time.sleep(0.5)                 # delay 0.5 seconds
        GPIO.output(red_pin1, False)
        GPIO.output(red_pin2, True)
        time.sleep(0.5)
finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.
