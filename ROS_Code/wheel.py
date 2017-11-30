#!/usr/bin/env python
#import dependencies
from __future__ import print_function
import pycreate2
import time

import rospy
from std_msgs.msg import Int32

#initiate variable, call back function update x
x=0
def callback(msg):
    print (msg.data)
    global x
    x = msg.data

#initiate subscriber
rospy.init_node('wheel')

sub = rospy.Subscriber('navigator', Int32, callback)

#config usb port
port = '/dev/ttyUSB0'

bot = pycreate2.Create2(port=port, baud=115200)

#	bot.start()
#	bot.safe()

#drive roomba
while not rospy.is_shutdown():
	bot.drive_direct(100,100)
	if x==1: #clockwise
		while x!=0 and  not rospy.is_shutdown():
                  bot.drive_direct(50,-50)
	if x==2: #counter clockwise
        	while x!=0 and not rospy.is_shutdown():
                  bot.drive_direct(-50,50)


rospy.spin()

