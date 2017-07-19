#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

try:
	while True:
		GPIO.output(11, GPIO.HIGH)
		sleep(2.5)
		GPIO.output(11, GPIO.LOW)
		sleep(2.5)
finally: 
	GPIO.cleanup()
exit()