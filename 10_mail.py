# 10_email_notifier.py

import RPi.GPIO as GPIO
import smtplib, time

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

GPIO.setmode(GPIO.BCM)
red_pin = 18
green_pin = 23
switch_pin = 24

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_email(username, password, recipient, subject, text):
    print(username, password, recipient, subject, text)
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(username, password)
    header = 'To:' + recipient + '\n' + 'From: ' + username
    header = header + '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(username, recipient, msg)
    smtpserver.close()

def green():
    GPIO.output(green_pin, True)
    GPIO.output(red_pin, False)

def red():
    GPIO.output(green_pin, False)
    GPIO.output(red_pin, True)

username = raw_input("Sending gmail address? ")
password = raw_input("Sending gmail password? ")
recipient = raw_input("Send email to? ")
subject = raw_input("Subject? ")
message = raw_input("Message ? ")

print("Press the button to send the Email")

while True:
    green()
    if GPIO.input(switch_pin) == False:
        red()
        send_email(username, password, recipient, subject, message)
        time.sleep(3)
        print("Press the button to send the Email")
        