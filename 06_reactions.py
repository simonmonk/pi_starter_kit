# 10_email_notifier.py

import RPi.GPIO as GPIO
import time, random

GPIO.setmode(GPIO.BCM)
red_pin = 18
green_pin = 23
red_switch_pin = 24
green_switch_pin = 25

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def green():
    GPIO.output(green_pin, True)
    GPIO.output(red_pin, False)

def red():
    GPIO.output(green_pin, False)
    GPIO.output(red_pin, True)

def off():
    GPIO.output(green_pin, False)
    GPIO.output(red_pin, False)

def key_pressed():
    if GPIO.input(red_switch_pin) and GPIO.input(green_switch_pin):
        return 0
    if not GPIO.input(red_switch_pin) and not GPIO.input(green_switch_pin):
        return -1
    if not GPIO.input(red_switch_pin) and GPIO.input(green_switch_pin):
        return 1
    if GPIO.input(red_switch_pin) and not GPIO.input(green_switch_pin):
        return 2
        
while True:
    off()
    print("Press the button for red or green when one lights")
    delay = random.randint(3, 7)
    color = random.randint(1, 2)
    time.sleep(delay)
    if (color == 2):
        red()
    else:
        green()
    t1 = time.time()
    
    while not key_pressed():
        pass
    t2 = time.time()
    if key_pressed() != color :
        print("WRONG BUTTON")
    else:
        print("Time: " + str(int((t2 - t1) * 1000)) + " milliseconds")
