# 08_light_harp.py

import RPi.GPIO as GPIO
import time, math

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23
buzzer_pin = 24

GPIO.setup(buzzer_pin, GPIO.OUT)

def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.001)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, True)
    while not GPIO.input(b_pin):
        count = count + 1
    return count

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