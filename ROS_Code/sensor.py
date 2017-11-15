#!/usr/bin/env python

from __future__ import print_function
from pycreate2 import Create2
import time

import rospy
from std_msgs.msg import Int32MultiArray

rospy.init_node('IR_publisher')

pub = rospy.Publisher('IR_sensor',Int32MultiArray)

rate = rospy.Rate(2)

port = '/dev/ttyUSB0'
bot = Create2(port=port, baud=115200)

bot.start()
bot.full()
print('Starting ...')

while not rospy.is_shutdown():
	sensor_state = bot.get_sensors()

	time.sleep(0.1)
	x = sensor_state[35]
	y = (int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),int(x[5]),)
	z = Int32MultiArray(data=y)
	pub.publish(z)
	rate.sleep()

