#!/usr/bin/env python
import rospy
import math
import time
import turtlesim.srv
from hw1.msg import Max
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from geometry_msgs.msg import Point
from foundations_hw1.srv import *

def callback(data):
    #rospy.loginfo(data)
    global px
    global py
    px=data.x
    py=data.y
    #rospy.loginfo((px,py))

def run():
    rospy.init_node('p5c')
    global px
    global py
    px=py=0
    full_param_name = rospy.search_param('location')
    loc = rospy.get_param(full_param_name)
    full_param_name = rospy.search_param('turtlename')
    name = rospy.get_param(full_param_name)
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(0, loc, 0, name)
    if loc==0:
        rospy.wait_for_service('kill')
        killer = rospy.ServiceProxy('kill', turtlesim.srv.Kill)
        killer('turtle1')
    #rospy.loginfo(loc)
    rospy.Subscriber(name+'/pose', Pose, callback)
    pub = rospy.Publisher(name+'/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    message = Twist()
    
    while not rospy.is_shutdown():
        rospy.wait_for_service('/reward')
        #rospy.loginfo((px,py))
        R = rospy.ServiceProxy('/reward', Reward)
        p1=Point(px,py,0)
        #rospy.loginfo(p1)
        p2=Point(px+0.01,py,0)
        #rospy.loginfo(p2)
        p3=Point(px,py+0.01,0)
        #rospy.loginfo(p3)
        f=R(p1).value
        f1=R(p2).value
        f2=R(p3).value
        g1=(f1-f)/0.01
        g2=(f2-f)/0.01
        Max.x=g1
        Max.y=g2
        #rospy.loginfo(Max)
        pub1 = rospy.Publisher('/gradient', Max, queue_size=10)
        message.linear.x = 1
        message.linear.y = 0
        message.linear.z = 0
        message.angular.x = 0
        message.angular.y = 0
        message.angular.z = 0
        
        pub.publish(message)
        
        rate.sleep()

if __name__ == '__main__':
    run()