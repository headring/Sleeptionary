import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

try:
	while True :
<<<<<<< HEAD
		if GPIO.input(22) == 0:
			print "good!"
		if GPIO.input(23) == 0:
			print "normal"
		if GPIO.input(24) == 0:
			print "bad"
		time.sleep(3)
=======
		if GPIO.input(22)==0:
			print "good!"
		if GPIO.input(23)==0:
			print "normal"
		if GPIO.input(24)==0:
			print "bad"

	time.sleep(1)

#print “Press the button (CTRL-C to exit)”
>>>>>>> 1821e275feff8f15971531a67d45af839d9775ab

except KeyboardInterrupt:
	GPIO.cleanup()
