import RPi.GPIO as GPIO
import time

frequency = 10 # Hz
wavelength = 1/frequency * 1000
gpio_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin,GPIO.OUT,initial=GPIO.LOW)

while True:
    GPIO.output(gpio_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(gpio_pin,GPIO.LOW)
    time.sleep(wavelength)