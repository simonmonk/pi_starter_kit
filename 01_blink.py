# 01_blink.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
red_pin = 18

GPIO.setup(red_pin, GPIO.OUT)
        
while True:
    GPIO.output(red_pin, True)
    time.sleep(0.5)
    GPIO.output(red_pin, False)
    time.sleep(0.5)