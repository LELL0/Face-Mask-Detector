# Face-Mask-Detector

 It's a Face Mask Detector, It detects the face of a person before entering a room. if the person has a mask he gets a hand sanitizer and the door opens in the other case the door stays locked a buzzer is activated to sound a beep and a mask is handed to the user then the user gets hand gel.


#######################################################################################################################

I worked on a Face mask Detector project, which is a RaspberryPi based project where I used multiple technologies like machine learning, python, the TensorFlow library and Raspbian OS which is a Linux operating system. A part of the code had the job to detect if a person has a mask or not, and based on the outcome I have another code that will run:

* if the person is wearing a face mask:
  it will wait for the individual to display his hand close to the sensor so the servo motor can press against the hand sanitizer and display it on his hand after so it will      unlock the door.



https://user-images.githubusercontent.com/81851926/154725387-e22d44f6-6144-45e7-9649-e031e64f1dad.mp4




* for the case where a face isn't detected it will wait for another attempt

* if a user isn't wearing a face mask it will make a beep sound using a buzzer, then displays a face mask with a stepper motor than the hand sanitizer similar to the first scenario.



https://user-images.githubusercontent.com/81851926/154726336-4aa79616-d873-44a4-b7c9-d3a4e6e2618c.mp4




(the steps are displayed on a small led screen so that the user knows what to do)


[FaceMaskDetector.drawio.pdf](https://github.com/Elia-El-Khoury/Face-Mask-Detector/files/8098627/FaceMaskDetector.drawio.pdf)
