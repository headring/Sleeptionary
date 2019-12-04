import RPi.GPIO as GPIO
import time
 
GPIO.setmode( GPIO.BOARD)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
request_count = int(raw_input("Enter Button Press Count ->"))
button_count = 0
 
while True :
           button_input = GPIO.input(11)
 
           if   button_input == False :
               button_count = button_count + 1
               print("Button Pressed ->%d"  %(button_count ) )
               time.sleep(1)
 
               if  button_count >= request_count :
                      break
 
GPIO.cleanup()
print ("Button Press Ended")

#22, 23, 24

