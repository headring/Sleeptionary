import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(22) == GPIO.HIGH:
			print(22)
#	 	if GPIO.input(22) != 0:
# 			print("good!")
#		if GPIO.input(23) != 0:
#			print("normal")
#		if GPIO.input(24) != 0:
#			print("bad")
		sleep(3)

except KeyboardInterrupt:
	GPIO.cleanup()
