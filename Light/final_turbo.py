import RPi.GPIO as GPIO
import time

pin = 27  # PWM pin num 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0

file = open("light_info.txt", mode='r')
file_line = file.readlines()
light_thresh = 200

p.ChangeDutyCycle(0)

try:
    for l in file_line:
        if int(l) <= light_thresh:
            p.ChangeDutyCycle(14)
            time.sleep(1)
            p.ChangeDutyCycle(1)
            time.sleep(60)
        else:
            time.sleep(60)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()

