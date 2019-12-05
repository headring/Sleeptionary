import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
soundpin = 12
GPIO.setup(soundpin,GPIO.IN)

if __name__=="__main__":
	while(True):
		soundlevel = GPIO.input(soundpin)
		print "soundlevel",soundlevel
		sleep(0.005)