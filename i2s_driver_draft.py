import RPi.GPIO as GPIO
import time

frequency = 1000 # Hz
wavelength = 1/frequency * 1000
buzzer_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT,initial=GPIO.LOW)

while True:
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(wavelength)
    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(wavelength)