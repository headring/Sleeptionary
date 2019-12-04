import RPi.GPIO as GPIO
import time
 
GPIO.setmode( GPIO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
request_count = int(raw_input("Enter Button Press Count ->"))
button_count = 0
 
while True :
           button_input = GPIO.input(15)
 
           if   button_input == False :
               button_count = button_count + 1
               print("Button Pressed ->%d"  %(button_count ) )
               time.sleep(1)
 
               if  button_count >= request_count :
                      break
 
GPIO.cleanup()
print ("Button Press Ended")

<<<<<<< HEAD
#15, 16, 18(pin #)
=======
#22, 23, 24

>>>>>>> 631db536ff2f5e9eac5c90465284f5b929789985
