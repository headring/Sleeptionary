import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

try:
	while True :
		if GPIO.input(22) == 0:
			print "good!"
		if GPIO.input(23) == 0:
			print "normal"
		if GPIO.input(24) == 0:
			print "bad"
		time.sleep(3)

except KeyboardInterrupt:
	GPIO.cleanup()
