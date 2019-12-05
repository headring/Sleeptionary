import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
soundpin = 12
GPIO.setup(soundpin,GPIO.IN)
CHECK_ON=1

try:
	while True:
		if GPIO.input(soundpin)==CHECK_ON:
			print "detect"
			time.sleep(1)
	finally:
		GPIO.cleanup()