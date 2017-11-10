#!/usr/bin/env python
import rospy
import math
import sys
import random
import turtlesim.srv
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from turtlesim.msg import Pose

def callback(data):
    #rospy.loginfo(data)
    global posx
    global posy
    global postheta
    posx=data.x
    posy=data.y
    postheta=data.theta

def run():
    rospy.init_node('p5b')
    global posx
    global posy
    global postheta
    posx=posy=postheta=0
    full_param_name = rospy.search_param('location')
    loc = rospy.get_param(full_param_name)
    full_param_name = rospy.search_param('turtlename')
    name = rospy.get_param(full_param_name)
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(5.5444444+loc, 5.5444444, math.pi/2, name)
    if loc<0:
        rospy.wait_for_service('kill')
        killer = rospy.ServiceProxy('kill', turtlesim.srv.Kill)
        killer('turtle1')
    rospy.Subscriber(name+'/pose', Pose, callback)
    pub = rospy.Publisher(name+'/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    message=Twist()
    
    while not rospy.is_shutdown():
        if loc<0:
            x=random.uniform(0,4)
            y=random.uniform(0,2*5.5444444)
            
            distance = math.sqrt((x - posx) ** 2 + (y - posy) ** 2)
            if distance>1.5:
                lin=distance*0.3
                ang=math.atan2(y-posy,x-posx)-postheta
            else:
                lin=0
                ang=0

            rospy.set_param('L',lin)
            rospy.set_param('A',ang)
            
            message.linear.x = lin
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = ang
        
            pub.publish(message)
        else:
            full_param_name = rospy.search_param('L')
            li = rospy.get_param(full_param_name)
            full_param_name = rospy.search_param('A')
            an = rospy.get_param(full_param_name)
            an=-1*an
        
            message.linear.x = li
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = an
        
            pub.publish(message)
            
        #tag=1
        #if abs(posx-5.5444444)>3:
        #        tag=1
        #else:
        #        tag=-1
        #rospy.wait_for_service(name+'/teleport_absolute')
        #turtle_teleport = rospy.ServiceProxy(name+'/teleport_absolute', turtlesim.srv.TeleportAbsolute)
        #turtle_teleport(xl,yl,0)
        
        
        rate.sleep()

if __name__ == '__main__':
    run()