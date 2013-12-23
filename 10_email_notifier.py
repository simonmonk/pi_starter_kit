# 10_email_notifier.py

# inspired by: http://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds

import RPi.GPIO as GPIO
import time, feedparser

GPIO.setmode(GPIO.BCM)

username = "username"     # before the @ sign
password = "password"     
 
NEWMAIL_OFFSET = 1        # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60      # check mail every 60 seconds
 
# GREEN_LED = 18
# RED_LED = 23
# GPIO.setup(GREEN_LED, GPIO.OUT)
# GPIO.setup(RED_LED, GPIO.OUT)
#  
# while True:
#  
#         newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
#  
#         if DEBUG:
#                 print "You have", newmails, "new emails!"
#  
#         if newmails > NEWMAIL_OFFSET:
#                 GPIO.output(GREEN_LED, True)
#                 GPIO.output(RED_LED, False)
#         else:
#                 GPIO.output(GREEN_LED, False)
#                 GPIO.output(RED_LED, True)
#  
#         time.sleep(MAIL_CHECK_FREQ)