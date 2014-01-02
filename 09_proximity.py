# 09_proximity.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23
led_pin = 24

threshold = 0

GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

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
        reading = step()
        GPIO.output(led_pin, (reading > threshold))

finally:  
    print("Cleaning up")
    GPIO.cleanup()