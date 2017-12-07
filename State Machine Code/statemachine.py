#!/usr/bin/env python

#import dependencies
from  __future__ import print_function
import pycreate2
import time

import rospy
from smach import State,StateMachine
from std_msgs.msg import Int32
from time import sleep

#define states
class Normal(State):
	def __init__(self):
		State.__init__(self, outcomes=['e'])

	def execute(self,userdata):
		while not rospy.is_shutdown():
       			bot.drive_direct(100,100)
			if x==3:
                        	return 'e' #Cliff
       			if x==1: #clockwise
               			while x!=0 and  not rospy.is_shutdown():
                		  bot.drive_direct(50,-50)
				  if x==3:
                        			return 'e' #Cliff
       			if x==2: #counter clockwise
                		while x!=0 and not rospy.is_shutdown():
                		  bot.drive_direct(-50,50)
				  if x==3:
			                        return 'e' #Cliff

class Emergency(State):
	def __init__(self):
		State.__init__(self, outcomes=['e'])

	def execute(self,userdata):
		while not rospy.is_shutdown():
			bot.drive_direct(0,0)
			if x!=3:
				return 'e' # return to normal

#define subscriber callback
x=0
def callback(msg):
	global x,x1
	x = msg.data

if __name__ == '__main__':
	rospy.init_node('state') #node
	sub = rospy.Subscriber('navigator', Int32, callback) #subscriber
	port = '/dev/ttyUSB0'
	bot = pycreate2.Create2(port=port, baud=115200) #serial port

	sm = StateMachine(outcomes=['normal']) #define state machine
	with sm:
		StateMachine.add('NORMAL', Normal(), transitions={'e':'EMERGENCY'})
		StateMachine.add('EMERGENCY',Emergency(),transitions={'e':'NORMAL'})

	sm.execute()
