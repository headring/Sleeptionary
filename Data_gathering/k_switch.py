import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.setup(18 , GPIO.IN)

print “Press the button”
try:

while True :

GPIO.output(23, False)
GPIO.output(24, False)
if GPIO.input(18)==0:
print ” Button pressed!”

GPIO.output(23, True)
GPIO.output(24, True)

time.sleep(1)

print “Press the button (CTRL-C to exit)”

except KeyboardInterrupt:
GPIO.cleanup()