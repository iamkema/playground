#!/usr/bin/python
# -*- coding: utf-8 -*-

# Pin reference
#   C1  |   7           
#   C2  |   11  12      
#   5   |   13  16      
#   6   |   15  18  |   17
#   7   |   29  22  |   16
#   8   |   31  31  |   15
#   9   |   33  36  |   14
#   10  |   35  38  |   13
#   11  |   37  40  |   12

import time
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# GPIO ports for the 7seg pins
segments =  (13,15,29,31,33,35,37,18,22,31,36,38,40)
# 7seg_digit_pins
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)

# GPIO ports for the common
common = (7,11)
# 7seg_digit_pins (1,2) digits 0-3 respectively
 
for digit in common:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)

# Establishing segment loop
seg1=(0, 13, 13, 0, 0, 0, 0)
#seg1=(0, 5, 5, 0, 0, 0, 0) #Pin based on 7 segment pins
seg2=(33, 31, 31, 33, 29, 29, 15)
#seg2=(9, 8, 8, 9, 7, 7, 6) #Pin based on 7 segment pins
seg3=(38, 40, 40, 38, 37, 37, 35)
#seg3=(13, 12, 12, 13, 11, 11, 10) #Pin based on 7 segment pins
seg4=(18, 22, 22, 18, 31, 31, 36)
#seg4=(17, 16, 16, 17, 15, 15, 14) #Pin based on 7 segment pins
c1=(7, 7, 0, 0, 0, 7, 7)
#c1=(1, 1, 0, 0, 0, 1, 1) #Pin based on 7 segment pins
c2=(0, 0, 11, 11, 11, 0, 0)
#c2=(0, 0, 2, 2, 2, 0, 0) #Pin based on 7 segment pins
all_seg=[seg1,seg2,seg3,seg4]

# Establishing high-low status per number
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

all_seg=[seg1,seg2,seg3,seg4]
sleep_t=0.001

try:
    while True:
        n = time.ctime()[11:13]+time.ctime()[14:16]
        s = str(n).rjust(4)
        for a in range(4):
           for b in range (0,7):
               pin_no=all_seg[a][b]
               if (pin_no == 0):
                    GPIO.output(13, 0)
                    else
                    GPIO.output(pin_no, num[s[a]][b])
               GPIO.output(7, c1[b])
               GPIO.output(11, c2[b])
               time.sleep(sleep_t)
finally:
    GPIO.cleanup()
