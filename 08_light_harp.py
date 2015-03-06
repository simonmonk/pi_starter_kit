# 08_light_harp.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time, math

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in series
# pin b discharges the capacitor through a fixed 1k resistor 
a_pin = 18
b_pin = 23
buzzer_pin = 24

GPIO.setup(buzzer_pin, GPIO.OUT)

# empty the capacitor ready to start filling it up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.001)

# return the time taken for the voltage on the capacitor to count as a digital input HIGH
# than means around 1.65V
# In this project, the return value is not used. The time taken for this function itself to run
# directly influenced the buzzer tome (see next comment block)
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, True)
    while not GPIO.input(b_pin):
        count = count + 1
    return count

# Rather misleadingly, this function actually makes the tone on the buzzer
# by turning it on and off, with a delay caused by charge_time.
# Cunning or what?
def analog_read():
    discharge()
    GPIO.output(buzzer_pin, True)
    discharge()
    charge_time()
    GPIO.output(buzzer_pin, False)
    charge_time()

try:
    while True:
        analog_read()

finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.