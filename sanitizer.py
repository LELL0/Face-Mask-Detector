import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

trigger = 31
echo = 33

Pin_servo=29


###################################

def setupServo():
    GPIO.setup(Pin_servo, GPIO.OUT)

def resetServo():
    p = GPIO.PWM(Pin_servo, 50)
    p.start(0)
    
def turnServo(angle):
    p = GPIO.PWM(Pin_servo, 50)     # angle 55 for 3 o clock  (locked)
    duty= angle / 18 + 2
    GPIO.output(Pin_servo,True)     # angle 150 for 12 o clock (unlocked)
    p.start(duty)
    time.sleep(0.35)
    GPIO.output(Pin_servo,False)
    p.ChangeDutyCycle(0)
    
###################################

def inputToFileSanitize(Data):
    f=open("Sanitize.txt","w")
    f.write(str(Data))
    f.close()

def getFromFileSanitize():
    f = open("Sanitize.txt","r")
    Data = f.readline()
    f.close()
    return Data

###################################
    
def setupUltraSonic():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trigger,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)

def getDistance():
    GPIO.output(trigger,0)
    time.sleep(0.5)
    GPIO.output(trigger,1)
    time.sleep(0.00001)
    GPIO.output(trigger,0)
    start = time.time()
    while GPIO.input(echo) == 0:
        start = time.time()
    while GPIO.input(echo) == 1:
        stop = time.time()
    elapsed = stop - start
    distance = elapsed * 17150
    return int(distance)

setupServo()
resetServo()
inputToFileSanitize('wait')
setupUltraSonic()
print('waiting')
while True:
    print(getFromFileSanitize(),' and ',getDistance())
    
    if getFromFileSanitize() == 'go' and getDistance() <= 10:
#    if getFromFileSanitize() == 'go':
        print('Die Microbes')
        time.sleep(1)
        turnServo(55)
        turnServo(150)
        time.sleep(1)
        resetServo()
        inputToFileSanitize('wait')
        print('waiting')