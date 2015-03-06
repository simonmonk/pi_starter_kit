# 06_reactions.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time, random

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# pins used for the LED and switches
red_pin = 18
green_pin = 23
red_switch_pin = 24
green_switch_pin = 25

# LED pins outputs, switch pins inputs
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# The next three functions turn appropriate LEDs on and off
def green():
    GPIO.output(green_pin, True)
    GPIO.output(red_pin, False)

def red():
    GPIO.output(green_pin, False)
    GPIO.output(red_pin, True)

def off():
    GPIO.output(green_pin, False)
    GPIO.output(red_pin, False)

# find which buttons pressed -1 means neither, 0=both, 1=red, 2=green 
def key_pressed():
    # if button is pressed GPIO.input will report false for that input
    if GPIO.input(red_switch_pin) and GPIO.input(green_switch_pin):
        return 0
    if not GPIO.input(red_switch_pin) and not GPIO.input(green_switch_pin):
        return -1
    if not GPIO.input(red_switch_pin) and GPIO.input(green_switch_pin):
        return 1
    if GPIO.input(red_switch_pin) and not GPIO.input(green_switch_pin):
        return 2

try:        
    while True:
        off()
        print("Press the button for red or green when one lights")
        delay = random.randint(3, 7)    # random delay of 3 to 7 seconds
        color = random.randint(1, 2)    # random color red=1, green=2
        time.sleep(delay)
        if (color == 2):
            red()
        else:
            green()
        t1 = time.time()
        while not key_pressed():
            pass
        t2 = time.time()
        if key_pressed() != color :   # check the right buton was pressed
            print("WRONG BUTTON")
        else:
            # display the response time
            print("Time: " + str(int((t2 - t1) * 1000)) + " milliseconds")
finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.
    
