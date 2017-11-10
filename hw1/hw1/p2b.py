#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
from std_msgs.msg import Int64MultiArray
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data)

def listen():
    rospy.init_node('p2b')
    while not rospy.is_shutdown():
        if sys.argv[2]=='geometry_msgs/Twist':
            rospy.Subscriber(sys.argv[1], Twist, callback)
        elif sys.argv[2]=='geometry_msgs/Point':
            rospy.Subscriber(sys.argv[1], Point, callback)
        elif sys.argv[2]=='std_msgs/Float64':
            rospy.Subscriber(sys.argv[1], Float64, callback)
        elif sys.argv[2]=='std_msgs/Int64MultiArray':
            rospy.Subscriber(sys.argv[1], Int64MultiArray, callback)
        elif sys.argv[2]=='std_msgs/String':
            rospy.Subscriber(sys.argv[1], String, callback)
        else:
            rospy.loginfo('Error Input!')
            break;

if __name__ == '__main__':
    listen()