import RPi.GPIO as GPIO  
from time import sleep



GPIO.setmode(GPIO.BOARD) 

GPIO.setup(12, GPIO.OUT) 

p = GPIO.PWM(12, 50)   

p.start(0)            

p.ChangeDutyCycle(3) 
sleep(1)

p.ChangeDutyCycle(12)
sleep(1) 

p.ChangeDutyCycle(7.5)
sleep(1)



while(1):

  val = float(raw_input("input(3~7.5~12) = "))
  
  if val == -1: break

  p.ChangeDutyCycle(val)
  

p.stop()                

GPIO.cleanup()