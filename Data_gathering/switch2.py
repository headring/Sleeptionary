import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(22) != 0:
		print(22)
		sleep(3)
	if GPIO.input(23) != 0:
		print(23)
		sleep(3)
	if GPIO.input(24) != 0:
		print(24)
		sleep(3)
