import RPi.GPIO as GPIO
import time
import drivers
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
Pin_Button= 35
GPIO.setup(Pin_Button, GPIO.IN)
    
while True:
    print(GPIO.input(Pin_Button))
    time.sleep(0.02)
    