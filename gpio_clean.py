#!/usr/bin/python
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
print "Cleaning GPIO..."
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.cleanup()
print "DONE!"
exit()