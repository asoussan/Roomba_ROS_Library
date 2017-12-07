#!/usr/bin/env python

#import dependencies
from __future__ import print_function
import time

import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32

#config variables
cw = 0
x = [0,0,0,0,0,0]

#call back function - update sensor data
def callback(msg):
    print (msg.data)
    global x,x1,x2 
    x = msg.data #sensor data
    x1 = x[0]+x[1]+x[2]+x[3]+x[4]+x[5] #x1!=0 when obstacle == 1
    x2 = x[6]+x[7]+x[8]+x[9] #x2!=0 when cliff is detected

rospy.init_node('navigator')

#subscriber and publisher
sub = rospy.Subscriber('IR_sensor', Int32MultiArray, callback)
pub = rospy.Publisher('navigator',Int32,queue_size=10)
rate = rospy.Rate(2)

#control logic
x2=0
while not rospy.is_shutdown():
  if x2 == 0:
        cw=0
	pub.publish(cw) #go straight
        if x[0]+x[1]+x[2]<x[3]+x[4]+x[5]: #if more obstacles on the right
                while x1!=0 and (not rospy.is_shutdown()): #when obstacle persists and ros is running
                  cw=1 #rotate clockwise
		  pub.publish(cw)
        if x[0]+x[1]+x[2]>x[3]+x[4]+x[5]: #if more obstacles on the left
                while x1!=0 and (not rospy.is_shutdown()):
                  cw=2 #rotate counter clockwise
		  pub.publish(cw)
  else:
	cw=3
	pub.publish(cw) #emergency

rospy.spin()
