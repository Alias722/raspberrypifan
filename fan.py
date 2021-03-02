#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

#init
FAN_PIN = 40
def fanControl(para):
    if para == "on" and nowstatus == False:
        GPIO.output(FAN_PIN,GPIO.HIGH)
        nowstatus = True
    elif para == "off" and nowstatus == True:
        GPIO.output(FAN_PIN,GPIO.LOW)
        nowstatus = False

#GPIO.setmode(GPIO.BCM)  #Board num
GPIO.setmode(GPIO.BOARD) #Pin num
GPIO.setup(FAN_PIN,GPIO.OUT)
nowstatus = False
#excute
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#loop
time1 = int(time.strftime("%S",time.localtime()))

print("time1 is : {}".format(time1))
input("Hello")
time2 = int(time.strftime("%S",time.localtime()))

try:
    while time2-time1 < 10:
        if time1 > time2:
            time1 -= 60
        time2 = int(time.strftime("%S",time.localtime()))
        print(time2-time1)
        fanControl("on")
except:
    GPIO.cleanup()
print("Finished")
GPIO.cleanup()
