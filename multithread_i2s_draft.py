import RPi.GPIO as GPIO
import threading
import time

exitFlag = 0

frequency = 10_000_000 # Hz
wavelength = 1/frequency
halfwave = wavelength / 2
gpio2 = 2
gpio3 = 3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(gpio3,GPIO.OUT,initial=GPIO.LOW)

class myThread (threading.Thread):
   def __init__(self, threadID, name, gpio):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.gpio = gpio
   def run(self):
      write_binary50_50(self.gpio)

def write_binary50_50(gpio):
   while True:
      GPIO.output(gpio,GPIO.HIGH)
      time.sleep(halfwave)
      GPIO.output(gpio,GPIO.LOW)
      time.sleep(halfwave)

# Create new threads
thread1 = myThread(1, 'GPIO2', gpio2)
thread2 = myThread(2, 'GPIO3', gpio3)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")