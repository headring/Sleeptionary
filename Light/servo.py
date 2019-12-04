import RPi.GPIO as GPIO
import time
 
pin = 18 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0
try:
    while True:
        p.ChangeDutyCycle(1)
        print "angle : 1"
        time.sleep(1)
        p.ChangeDutyCycle(5)
        print "angle : 5"
        time.sleep(1)
        p.ChangeDutyCycle(8)
        print "angle : 8"
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()
