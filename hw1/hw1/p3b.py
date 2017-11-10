#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from geometry_msgs.msg import Point
from foundations_hw1.srv import *

def callbackchase(data):
    global chasex
    global chasey
    chasex=data.x
    chasey=data.y
    #rospy.loginfo(data)
    
def callback(data):
    global runx
    global runy
    runx=data.x
    runy=data.y
    
def callbackescape(data):
    global runx
    global runy
    global runner
    global chasex
    global chasey
    chasex=chasey=0
    runx=runy=0
    runner=data.name
    #rospy.loginfo(runner)
    rospy.Subscriber(runner+'/pose', Pose, callback)
    #rospy.loginfo(runx)
    #rospy.loginfo(runy)
    time.sleep(0.5)
    rospy.Subscriber('turtle1/pose', Pose, callbackchase)
    #rospy.loginfo(chasex)
    #rospy.loginfo(chasey)
    if runx<chasex and runy<chasey:
        pointx=0
        pointy=11
    elif runx<chasex and runy>chasey:
        pointx=0
        pointy=0
    elif runx>chasex and runy>chasey:
        pointx=11
        pointy=0
    else:
        pointx=11
        pointy=11
    point=Point(pointx,pointy,0)
    #rospy.loginfo(point)
    return EscapeResponse(point)
    

def escape_server():
    rospy.init_node('escape_server')
    
    s=rospy.Service('/escape', Escape, callbackescape)
    
    rospy.spin()
    
if __name__ == '__main__':
    escape_server()
