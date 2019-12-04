import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

try:
    while True:
        inputIO = GPIO.input(21)

        if inputIO == False:
            GPIO.output(6, GPIO.HIGH)
            #time.sleep(1)

        else:
            GPIO.output(6, GPIO.LOW)
            #time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()