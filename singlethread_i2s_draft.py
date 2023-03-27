import RPi.GPIO as GPIO
import time

frequency = 10 # Hz
wavelength = 1/frequency
halfwave = wavelength / 2
gpio2 = 2
gpio3 = 3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(gpio3,GPIO.OUT,initial=GPIO.LOW)

while True:
    GPIO.output(gpio2,GPIO.HIGH)
    GPIO.output(gpio3,GPIO.HIGH)
    time.sleep(halfwave)
    GPIO.output(gpio2,GPIO.LOW)
    time.sleep(halfwave)
    time.sleep(halfwave)