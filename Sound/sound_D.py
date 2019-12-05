import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
soundpin = 12
GPIO.setup(soundpin,GPIO.IN)

while True:
	if GPIO.input(soundpin) == 1 :
		print "detect"
