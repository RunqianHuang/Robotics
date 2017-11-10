#!/usr/bin/env python
import rospy
import math
import sys
import turtlesim.srv
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(data)

def run():
    rospy.init_node('p5a')
    full_param_name = rospy.search_param('location')
    loc = rospy.get_param(full_param_name)
    full_param_name = rospy.search_param('turtlename')
    name = rospy.get_param(full_param_name)
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(2+loc, 9.1-loc, 0, name)
    if loc==0:
        rospy.wait_for_service('kill')
        killer = rospy.ServiceProxy('kill', turtlesim.srv.Kill)
        killer('turtle1')
    rospy.Subscriber(name+'/pose', Pose, callback)
    pub = rospy.Publisher(name+'/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(0.5)
    
    message = Twist()
    
    i=0
    while i<10:
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
            message.angular.z = math.pi/2
        i=i+1
        
        pub.publish(message)
        
        rate.sleep()

if __name__ == '__main__':
    run()