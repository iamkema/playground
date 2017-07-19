#!/usr/bin/python
# -*- coding: utf-8 -*-

# Pin reference
#	C1	|	7			
#	C2	|	11	12		
#	5	|	13	16		
#	6	|	15	18	|	17
#	7	|	29	22	|	16
#	8	|	31	31	|	15
#	9	|	33	36	|	14
#	10	|	35	38	|	13
#	11	|	37	40	|	12


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

sleep_time=0.1

finally:
	GPIO.cleanup()

seg1=[0, 5, 5, 0, 0, 0, 0]
seg2=[9, 8, 8, 9, 7, 7, 6]
seg3=[13, 12, 12, 13, 11, 11, 10]
seg4=[17, 16, 16, 17, 15, 15, 14]
c1=[1, 1, 0, 0, 0, 1, 1]
c2=[0, 0, 2, 2, 2, 0, 0]

i=0
seq_group=[]
while ( i <= 6 ):
	seq=[]
	seq.append(seg1[i])
	seq.append(seg2[i])
	seq.append(seg3[i])
	seq.append(seg4[i])
	seq.append(c1[i])
	seq.append(c2[i])
	i+=1
	seq_group.append(seq)
