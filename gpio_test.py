#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

sleep_time=0.02
try:
	i=1
	while i <= 5:
		while True:
			GPIO.output(11, GPIO.HIGH)
			#print "GPIO_11 HIGH"
			sleep (sleep_time)
			GPIO.output(11, GPIO.LOW)
			#print "GPIO_11 LOW"
			sleep (sleep_time);
		sleep (1)
		print "%d Seconds" % i
		i=i+1;
finally: 
	GPIO.cleanup()
exit()