#!/usr/bin/env python

#import dependencies
from __future__ import print_function
from pycreate2 import Create2
import time

import rospy
from std_msgs.msg import Int32MultiArray

#initiate ROS node
rospy.init_node('IR_publisher')

#publisher
pub = rospy.Publisher('IR_sensor',Int32MultiArray)

rate = rospy.Rate(2)

#config USB port
port = '/dev/ttyUSB0'
bot = Create2(port=port, baud=115200)

#start Roomba
bot.start()
bot.full()
print('Starting ...')

#read sensor and publish sensor readings
while not rospy.is_shutdown():
	sensor_state = bot.get_sensors()

	time.sleep(0.1)
	x = sensor_state[35] #IR sensor
	y = (int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),int(x[5]),) #repack date into array
	z = Int32MultiArray(data=y)
	pub.publish(z) #publish array
	rate.sleep()

