#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(data)

def run():
    rospy.init_node('p2d')
    rospy.Subscriber('turtle1/pose', Pose, callback)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    
    message = Twist()
    
    i=0
    while i<15:
        if i%2==0:
            message.linear.x = 2
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = 0
        else:
            message.linear.x = 0
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = 2*math.pi/7
        i=i+1
        
        pub.publish(message)
        
        rate.sleep()

if __name__ == '__main__':
    run()