# 05_thermomether_plus.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from Tkinter import *           # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time, math


C = 0.38 # uF - Tweek this value around 0.33 to improve accuracy
R1 = 1000 # Ohms
B = 3800.0 # The thermistor constant - change this for a different thermistor
R0 = 1000.0 # The resistance of the thermistor at 25C -change for different thermistor


# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# This project uses a thermistor, a component whose resistance varies with the temperature.
# To measure its resistance, the code records the time it takes for a capacitor to fill  
# when supplied by a current passing through the resistor. The lower the resistance the faster 
# it fills up. 
#
# You can think of a capacitor as a tank of electricity, and as it fills with charge, the voltage
# across it increases. We cannot measure that voltage directly, because the Raspberry Pi
# does not have an analog to digital convertor (ADC or analog input). However, we can time how long it
# takes for the capacitor to fill with charge to the extent that it gets above the 1.65V or so
# that counts as being a high digital input. 
# 
# For more information on this technique take a look at: 
# learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi
# The code here is based on that in the Raspberry Pi Cookbook (Recipes 12.1 to 12.3)


# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in series
# pin b discharges the capacitor through a fixed 1k resistor 

a_pin = 18
b_pin = 23
buzzer_pin = 24

GPIO.setup(buzzer_pin, GPIO.OUT)

set_temp = 25           # The temperature above which the buzzer will sound

# The type of capacitors only have an accuracy of +-10% on its stated value and there are 
# other components that will not be exactly the value stated on the package
# changing the fiddle_factor will help compensate for this.
# fiddle with the fiddle_factor (keep it close to 1.0) until this project agrees with a 
# thermometer you trust.
# To be honest, its never going to be very accurate, as an absolute thermometer,
# but the value of temp should increase when you hold the thermistor between you fingers to
# warm it up.

# empty the capacitor ready to start filling it up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)

# return the time taken for the voltage on the capacitor to count as a digital input HIGH
# than means around 1.65V
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000 # microseconds

# Take an analog readin as the time taken to charge after first discharging the capacitor
def analog_read():
    discharge()
    t = charge_time()
    discharge()
    return t

# Convert the time taken to charge the cpacitor into a value of resistance
# To reduce errors, do it lots of times and take the average.
def read_resistance():
    n = 10
    total = 0;
    for i in range(0, n):
        total = total + analog_read()
    t = total / float(n)
    T = t * 0.632 * 3.3
    r = (T / C) - R1
    return r



def read_temp_c():
    R = read_resistance()
    t0 = 273.15     # 0 deg C in K
    t25 = t0 + 25.0 # 25 deg C in K
    # Steinhart-Hart equation - Google it
    inv_T = 1/t25 + 1/B * math.log(R/R0)
    T = (1/inv_T - t0)
    return T

# sound the buzzer at a certain pitch (in Hz) for a duration in seconds
def buzz(pitch, duration):
	period = 1.0 / pitch            # period of cycle
	delay = period / 2              # delay half of period (2 delays per cycle)
	cycles = int(duration * pitch)  # total number of cycles needed for duration specified
	for i in range(cycles):         # turn buzzer on and off for number of cycles needed
		GPIO.output(buzzer_pin, True)
		time.sleep(delay)
		GPIO.output(buzzer_pin, False)
		time.sleep(delay)

# group together all of the GUI code into a class called App
class App:

    # this function gets called when the app is created
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Temp C', font=("Helvetica", 32))
        label.grid(row=0)
        self.reading_label = Label(frame, text='12.34', font=("Helvetica", 110))
        self.reading_label.grid(row=1)
        self.update_reading()

    # Update the temperature reading
    def update_reading(self):
        temp_c = read_temp_c()
        if temp_c > set_temp:
            buzz(500, 0.3)
        reading_str = "{:.2f}".format(temp_c)
        self.reading_label.configure(text=reading_str)
        self.master.after(500, self.update_reading)

# Set the GUI running, give the window a title, size and position
root = Tk()
root.wm_title('Thermometer')
app = App(root)
root.geometry("400x300+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()
