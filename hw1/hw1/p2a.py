#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(data)

def run():
    rospy.init_node('p2a')
    rospy.Subscriber('turtle1/pose', Pose, callback)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    
    message = Twist()
    
    while not rospy.is_shutdown():
        message.linear.x = 5
        message.linear.y = 0
        message.linear.z = 0
        message.angular.x = 0
        message.angular.y = 0
        message.angular.z = math.pi/2
        
        pub.publish(message)
        
        rate.sleep()

if __name__ == '__main__':
    run()