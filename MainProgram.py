import RPi.GPIO as GPIO
import time
import drivers
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

trigger = 31
echo = 33

Pin_buzzer=37

Pin_servo=7

Pin_Button=35

####motor#####
P_A1 = 32  # adapt to your wiring
P_A2 = 36 # ditto
P_B1 = 38 # ditto
P_B2 = 40 # ditto
delay = 0.005 # time to settle
#########################################################################################################
def setupMotor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_A1, GPIO.OUT)
    GPIO.setup(P_A2, GPIO.OUT)
    GPIO.setup(P_B1, GPIO.OUT)
    GPIO.setup(P_B2, GPIO.OUT)
    
def setStepper(in1, in2, in3, in4):
    GPIO.output(P_A1, in1)
    GPIO.output(P_A2, in2)
    GPIO.output(P_B1, in3)
    GPIO.output(P_B2, in4)
    time.sleep(delay)
    
def forwardStep():
    setStepper(1, 0, 1, 0)
    setStepper(0, 1, 1, 0)
    setStepper(0, 1, 0, 1)
    setStepper(1, 0, 0, 1)

def backwardStep():
    setStepper(1, 0, 0, 1)
    setStepper(0, 1, 0, 1)
    setStepper(0, 1, 1, 0)
    setStepper(1, 0, 1, 0)
    
#####################################
def forwardMotor(k):  # k is the number of steps
    print ("Giving A Mask") #512 steps for 360 degrees
    for i in range(k):
        forwardStep()
        
def backwardMotor(k):   
    print("backward")
    for i in range(k):
        backwardStep()
#########################################################################################################
display = drivers.Lcd()

def lcdMaskOn(txt1,txt2):
    display.lcd_display_string(txt1, 1)
    display.lcd_display_string(txt2, 2)
    display.lcd_backlight(1)
   
   
def lcdMaskOff():
    display.lcd_clear()
    display.lcd_backlight(0)
    
lcdMaskOff()
lcdMaskOn('Please Wait...','Loading Program')
#########################################################################################################   
import cv2

def takePic():
    img_counter = 0
    f=0
    f = open("imgcounter.txt","r")
    img_counter = int(f.readline())
    f.close()
    name = 'People'
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)
    ret, frame = cam.read()
    cv2.imshow("press space to take a photo", frame)
    img_name = name +"/image_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    time.sleep(0.2)
    f = open("imgcounter.txt", "w")
    f.write(str(img_counter))
    print("exiting...")
    f.close()
    
    cam.release()
    cv2.destroyAllWindows()
    
#########################################################################################################

    
def setupButton():
    GPIO.setup(Pin_Button, GPIO.IN)

def inputButtonLOOP():
    lcdMaskOn("press the button","to scan a face")
    while(not GPIO.input(Pin_Button)):
        time.sleep(0.1)
    print('button pressed')
    time.sleep(1)
    return 1
            
###################################
def timer(t0):      
    t1 = time.time()
    total = t1-t0
    return int(total)

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
    time.sleep(1)
    GPIO.output(Pin_servo,False)
    p.ChangeDutyCycle(0)
    
###################################
    
def setupBuzzer():
    GPIO.setup(Pin_buzzer, GPIO.OUT)

def buzz(sec):
    p = GPIO.PWM(Pin_buzzer, 4000)
    p.start(100)
    time.sleep(sec)
    p.stop()

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

def inputToFileWait(Data):
    f=open("Wait.txt","w")
    f.write(str(Data))
    f.close()
    
inputToFileWait('wait')

def getFromFileWait():
    f = open("Wait.txt","r")
    Data = f.readline()
    f.close()
    return Data

def getFromFileValue():
    f = open("Value.txt","r")
    Data = f.readline()
    f.close()
    return Data

def inputToFileTimer(Data):
    f=open("Timer.txt","w")
    f.write(str(Data))
    f.close()
    
def getFromFileTimer():
    f = open("Timer.txt","r")
    Data = f.readline()
    f.close()
    return Data

def inputToFileData(Data):
    f=open("Data.txt","w")
    f.write(str(Data))
    f.close()

def getFromFileData():
    f = open("Data.txt","r")
    Data = f.readline()
    f.close()
    return Data

###################################

def servoUnlock():
    setupServo()
    resetServo()
    time.sleep(2)
    turnServo(150)

def servoLock():
    setupServo()
    resetServo()
    time.sleep(2)
    turnServo(55)

def buzzUnlock():
    setupBuzzer()
    buzz(0.2)
    time.sleep(0.1)
    buzz(0.2)

def buzzLock():
    setupBuzzer()
    buzz(1.5)
    
###################################
def lcdMaskOn(txt1,txt2):
    display.lcd_display_string(txt1, 1)
    display.lcd_display_string(txt2, 2)
    display.lcd_backlight(1)
   
   
def lcdMaskOff():
    display.lcd_clear()
    display.lcd_backlight(0)
    
def lcdMaskTimer(txt1,txt2,timer):
    display.lcd_display_string(txt1, 1)
    display.lcd_display_string(txt2, 2)
    display.lcd_backlight(1)
    for i in range(0,timer):
        display.lcd_backlight(1)
        time.sleep(1)
        display.lcd_backlight(0)
        time.sleep(0.1)
        display.lcd_backlight(1)
        time.sleep(0.05)
        display.lcd_backlight(0)
        time.sleep(0.1)
    display.lcd_clear()
    display.lcd_backlight(0)

###################################


#wait for the machine learning to start

while getFromFileWait() == 'wait':
    time.sleep(0.1)

lcdMaskOff()
setupButton()
inputToFileTimer("stop")
inputToFileData(0)
setupMotor()
#################### Main Program ############################
while True:
    lcdMaskOff()
    if inputButtonLOOP():
        #print("taking a pic...")
        #takePic()
        #print("Done")
        inputToFileTimer("go")
        t0=time.time()
        lcdMaskOff()
        lcdMaskOn("Scanning A Face","Wear A Mask")
        try:
            while timer(t0)<=35:
                time.sleep(1)
                print(timer(t0))
        except:
            print("\nsomething went wrong exiting...")
            inputToFileTimer("stop")
            inputToFileData(0)
            lcdMaskOff()
            continue
        
        inputToFileTimer("stop")
        
        
        Value = int(getFromFileValue())
        if Value <= 0:
            lcdMaskTimer("Face Not Detected","",3)
            continue
        mask= int(getFromFileData())

        # The person has a mask on his face
        time.sleep(5)
        lcdMaskOff()
        print("face :",Value)
        print("mask :",mask)
        if mask>0:
            
            lcdMaskOn("Mask checked","Welcome!")
            buzzUnlock()
            lcdMaskOff()
            #waiting for sanitizer
            inputToFileSanitize("go")
            lcdMaskOff()
            lcdMaskOn("Before Entering","Sanitize Hands")
            while getFromFileSanitize()=='go':
                time.sleep(0.2)
            lcdMaskOff()
            servoUnlock()
            lcdMaskTimer("You Can Now","Enter The Room",3)
            time.sleep(10)
            servoLock()
            
        # The person does not have a mask on his face
        elif mask<=0:
            lcdMaskOn("Mask is Required","Take One ==>")
            buzzLock()
            forwardMotor(350)
            servoLock()
            lcdMaskOff()
        inputToFileSanitize("wait")