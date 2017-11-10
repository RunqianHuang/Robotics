#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from turtlesim.msg import Pose

def callback1(data):
    global tarx
    global tary
    tarx=data.x
    tary=data.y
    #rospy.loginfo(data)
    #rospy.loginfo(tarx)
    #rospy.loginfo(tary)
    
def callback2(data):
    global curx
    global cury
    global curang
    curx=data.x
    cury=data.y
    curang=data.theta
    #rospy.loginfo(data)
    #rospy.loginfo(curx)
    #rospy.loginfo(cury)
    #rospy.loginfo(curang)

def run():
    rospy.init_node('p2c')
    
    global tarx
    global tary
    global curx
    global cury
    global curang
    tarx=tary=curx=cury=curang=0;
    
    #time.sleep(1)
    rospy.Subscriber('/hw1/target_loc', Point, callback1)
    rospy.Subscriber('/turtle1/pose', Pose, callback2)
    #time.sleep(1)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    
    message = Twist()
    
    while not rospy.is_shutdown():
        if tarx>curx and tary>=cury:
            angle=math.atan2((tary-cury),(tarx-curx))
        elif tarx<curx and tary<cury:
            angle=math.atan2((tary-cury),(tarx-curx))+2*math.pi
        elif tarx<curx and tary>=cury:
            angle=math.atan2((tary-cury),(tarx-curx))
        elif tarx>curx and tary<cury:
            angle=math.atan2((tary-cury),(tarx-curx))+2*math.pi
        elif tarx==curx and tary>cury:
            angle=math.pi/2
        else:
            angle=3*math.pi/2
        #rospy.loginfo(tarx)
        #rospy.loginfo(tary)
        #rospy.loginfo(curx)
        #rospy.loginfo(cury)
        #rospy.loginfo(curang)
        #rospy.loginfo(angle)
        #rospy.loginfo(abs(angle-curang))
        if abs(angle-curang)<=math.pi/18:
            message.linear.x = 2
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = 0
        elif (angle-curang)>math.pi/18:
            message.linear.x = 0
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = math.pi/3
        else:
            message.linear.x = 0
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = -math.pi/3
        
        pub.publish(message)
        
        rate.sleep()

if __name__ == '__main__':
    run()