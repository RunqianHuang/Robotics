#!/usr/bin/env python
import rospy
import math
import time
import turtlesim.srv
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback(data):
    global initx
    global inity
    initx=data.x
    inity=data.y
    #rospy.loginfo(initx)
    #rospy.loginfo(inity)
    
def run():
    rospy.init_node('p3a')
    
    global initx
    global inity
    initx=inity=0;
    rospy.Subscriber('turtle1/pose', Pose, callback)
    #rospy.loginfo(initx)
    #rospy.loginfo(inity)
    time.sleep(0.5)
    rospy.wait_for_service('spawn')
    spawner1 = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner1(initx-3, inity, 0, 'turtle2')
    spawner2 = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner2(initx, inity-3, 0, 'turtle3')
    spawner3 = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner3(initx-3, inity-3, 0, 'turtle4')
    
    pub1 = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    pub2 = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)
    pub3 = rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=10)
    pub4 = rospy.Publisher('turtle4/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(0.5)
    
    message = Twist()
    
    i=0
    while not rospy.is_shutdown():
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
        if i>=10:
            break
        
        pub1.publish(message)
        pub2.publish(message)
        pub3.publish(message)
        pub4.publish(message)
        
        rate.sleep()

if __name__ == '__main__':
    run()