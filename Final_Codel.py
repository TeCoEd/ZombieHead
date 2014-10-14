##### TeCoEd Socrative Zombie #####
##### Screams at you #####

import time
import random
import RPi.GPIO as GPIO
import pygame

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

###CREATE A VARIABLE FOR THE PIR

PIR = 7
GPIO.setup(17, GPIO.OUT) ### LED PIN set up Earth on PIN 25
GPIO.setup(PIR, GPIO.IN) ### PIR PIN set up
GPIO.output(17, False)

def Motion_Sensing(PIR):
    
    time.sleep(0.3)
    list_of_sounds = str(random.randint(1,9))
    print "We see you"
    pygame.mixer.init(frequency=22050,size=-16,channels=4)
    sound = pygame.mixer.Sound("/home/pi/" + list_of_sounds + ".wav")
    sound.play()
    GPIO.output(17, True)
    time.sleep(0.3)
    GPIO.output(17, False)
    time.sleep(0.5)
    GPIO.output(17, True)
    time.sleep(0.3)
    GPIO.output(17, False)
    time.sleep(0.3)
    GPIO.output(17, True)
    time.sleep(1)
    GPIO.output(17, False)
    time.sleep(0.2)
    GPIO.output(17, True)
    time.sleep(0.2)
    GPIO.output(17, False)
    time.sleep(0.3)
    GPIO.output(17, True)
    time.sleep(0.2)
    GPIO.output(17, False)
    time.sleep(0.1)
    GPIO.output(17, True)
    time.sleep(0.1)
    GPIO.output(17, False)
    time.sleep(0.3)
    GPIO.output(17, True)
    time.sleep(1)
    GPIO.output(17, False)
    time.sleep(0.2)
    GPIO.output(17, True)
    time.sleep(0.2)
    GPIO.output(17, False)
    time.sleep(0.3)
    GPIO.output(17, True)
    time.sleep(0.1)
    GPIO.output(17, False)
    time.sleep(0.3)
    GPIO.output(17, True)
    time.sleep(0.1)
    GPIO.output(17, False)
    sound.stop()
    time.sleep(2)
    
print "Ready to find you"
time.sleep(1)

try:
    GPIO.add_event_detect(PIR, GPIO.RISING, callback=Motion_Sensing)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print "Quit"
    
