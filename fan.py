#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

#init

#FAN_PIN = 3

GPIO.setmode(GPIO.BCM)  #Board num
#GPIO.setmode(GPIO.BOARD) #Pin num

GPIO.setup(3,GPIO.OUT)
#excute
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#loop

while True:
    GPIO.output(3,GPIO.HIGH)

