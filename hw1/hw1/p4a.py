#!/usr/bin/env python
import rospy
import sys
import math
import random
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move(event):
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    message = Twist()
    message.linear.x = random.uniform(0,5)
    message.linear.y = 0
    message.linear.z = 0
    message.angular.x = 0
    message.angular.y = 0
    message.angular.z = random.uniform(-2*math.pi/2,2*math.pi/2)
    #rospy.loginfo(message)
    pub.publish(message)
    print 'Timer called at ' + str(event.last_duration)
    
def run():
    rospy.init_node('p4a')
    
    a=sys.argv[1]
    a=float(a)
    a=1/a
    #rospy.loginfo(a)
    rospy.Timer(rospy.Duration(a), move)
    rospy.spin()
    
if __name__ == '__main__':
    run()