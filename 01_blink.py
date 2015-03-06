# 01_blink.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com


import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

red_pin = 18

GPIO.setup(red_pin, GPIO.OUT)


try:         
    while True:
        GPIO.output(red_pin, True)  # LED on
        time.sleep(0.5)             # delay 0.5 seconds
        GPIO.output(red_pin, False) # LED off
        time.sleep(0.5)             # delay 0.5 seconds
finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
# You could get rid of the try: finally: code and just have the while loop
# and its contents. However, the try: finally: construct makes sure that
# when you CTRL-c the program to end it, all the pins are set back to 
# being inputs. This helps protect your Pi from accidental shorts-circuits
# if something metal touches the GPIO pins.
    