# Roomba ROS Library

### **_Tongdi Zhou_** 

  Temple University College of Engineering

  Advisor: Dr. Li Bai

### Introduction

This ROS library is created to control iRobot Create 2 connected to raspberry pi 3 through USB serial cable.
iRobot Roomba Create can be purchased from here: http://store.irobot.com/default/create-programmable-programmable-robot-irobot-create-2/RC65099.html?cgid=us
Raspberry Pi 3 can be purchased from here: https://www.raspberrypi.org/products/raspberry-pi-3-model-b/

### Prerequisites
1. This console cable(https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview) can be used to connect the raspberry with computer. The website also provides users with instructions on using the console cable.
2. This website (https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md) provides information about how to connect raspberry to WiFi.
3. Ubuntu should be installed into the raspberry pi. Installation instructiions and pertinent information can be found here: https://wiki.ubuntu.com/ARM/RaspberryPi
4. The instructions for installing ROS can be found here:http://wiki.ros.org/Installation/UbuntuARM make sure ROS Kinetic is installed.
5. A library to control iRobot Create 2 is required. This instructions to install this library is here: https://pypi.python.org/pypi/pycreate2/0.7.3

### Using ROS
1. Create workspace by using command lines:
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
2. Create a package in your workspace:
```
cd ~/catkin_ws/src
catkin_create_pkg roomba rospy
```
3. Go into folder 
```
cd ~/catkin_ws/src/roomba/src
```
and paste the ROS code in here using 
```
git clone https://github.com/Talisker10/Roomba_ROS_Library
```
Then go back to catkin_ws using `cd ~/catkin_ws`. Type command `source devel/setup.bash`

4. Open a new terminal window and log into your raspberry pi by using `ssh pi@ipaddress`. Run roscore: 
```
roscore
```
5. Open a second terminal window as the publisher: 
```
rosrun roomba sensor.py
```
6. Open a third terminal window as the navigator (subscriber and publisher)
```
rosrun roomba navigator.py
```
7. Open a third terminal window as the subscriber: 
```
rosrun roomba wheel.py
```
8. Now the roomba should be running while avoiding obstacles. Open another terminal, to list all active topics, use:
```
rostopic list
```
9.To check the message the publisher is sending, use:
```
rostopic echo IR_sensor
```
10.To find the publisher and the subscribers of the topic, use:
```
rostopic info IR_sensor
```
11.To find out more rostopic functions, use:
```
rostopic -h
```
### Flow Chart
![Flow Chart](https://github.com/Talisker10/Roomba_ROS_Library/blob/master/Figures/Flow%20Chart.jpg)
