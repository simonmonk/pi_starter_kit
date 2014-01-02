# 02_blink_twice.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
red_pin1 = 18
red_pin2 = 23

GPIO.setup(red_pin1, GPIO.OUT)
GPIO.setup(red_pin2, GPIO.OUT)
        
try:
    while True:
        GPIO.output(red_pin1, True)
        GPIO.output(red_pin2, False)
        time.sleep(0.5)
        GPIO.output(red_pin1, False)
        GPIO.output(red_pin2, True)
        time.sleep(0.5)
finally:  
    print("Cleaning up")
    GPIO.cleanup()