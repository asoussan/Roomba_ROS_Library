#!/usr/bin/env python

from __future__ import print_function
import pycreate2
import time

import rospy
from std_msgs.msg import Int32MultiArray

x = [0,0,0,0,0,0]

def callback(msg):
    print (msg.data)
    global x,x1 
    x = msg.data
    x1 = x[0]+x[1]+x[2]+x[3]+x[4]+x[5]

rospy.init_node('wheel')

sub = rospy.Subscriber('IR_sensor', Int32MultiArray, callback)


port = '/dev/ttyUSB0'  

bot = pycreate2.Create2(port=port, baud=115200)

#	bot.start()
#	bot.safe()
while not rospy.is_shutdown():
	bot.drive_direct(100,100)
	if x[0]+x[1]+x[2]<x[3]+x[4]+x[5]:
		while x1!=0 and (not rospy.is_shutdown()):
                  bot.drive_direct(50,-50) 
	if x[0]+x[1]+x[2]>x[3]+x[4]+x[5]:
        	while x1!=0 and (not rospy.is_shutdown()):	        
                  bot.drive_direct(-50,50)


rospy.spin()

