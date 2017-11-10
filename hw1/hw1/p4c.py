#!/usr/bin/env python
import rospy
import math
import time
from std_msgs.msg import Int32,String

def callback(data):
    #rospy.loginfo(data)
    global ratenum
    ratenum=data.data
    #rospy.loginfo(ratenum)

def run():
    rospy.init_node('p4c')
    global ratenum
    ratenum=1
    rospy.Subscriber('/pub_rate', Int32, callback)
    #time.sleep(0.5)
    pub = rospy.Publisher('/ping', String, queue_size=10)
    
    message = String
    
    while not rospy.is_shutdown():
        message='ping'
        rospy.loginfo(ratenum)
        rate = rospy.Rate(ratenum)
        pub.publish(message)
        
        rate.sleep()

if __name__ == '__main__':
    run()