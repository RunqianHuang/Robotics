#!/usr/bin/env python
import rospy
import math
import numpy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import UInt32MultiArray,Float64MultiArray,MultiArrayLayout,MultiArrayDimension

def findsubarray(data):
    num=len(data)
    maxsum=0
    maxbegin=0
    maxend=0
    summ=0
    for i in range(0,num-1):
        if summ<0:
            summ=0
            maxbegin=i
        summ=summ+data[i]
        if summ>=maxsum:
            maxsum=summ
            maxend=i
    #rospy.loginfo((maxbegin,maxend))
    return maxbegin,maxend,maxsum

def callback(data):
    #rospy.loginfo(data)
    rownum=data.layout.dim[0].size
    columnnum=data.layout.dim[1].size
    dataset=data.data
    subarrayset=[]
    #count=0
    for i in range(0,rownum-1):
        temp=[]
        for k in range(0,columnnum-1):
            temp.append(dataset[rownum*i+k])
        (x,y,z)=findsubarray(temp)
        #rospy.loginfo((x,y,z))
        for j in range(x,y):
            subarrayset.append(dataset[rownum*i+j])
            #count=count+y-x+1
            #rospy.loginfo(count)
    #rospy.loginfo(subarrayset)
    (begin,end,summary)=findsubarray(subarrayset)
    rospy.loginfo((begin,end,summary))
    outputdata=[begin,end]
    pub=rospy.Publisher('/hw1/subarray', UInt32MultiArray, queue_size=10)
    layout = MultiArrayLayout()
    layout.dim = [MultiArrayDimension('height', 1, 2 * 1),
                MultiArrayDimension('width', 2, 2)]
    pub.publish(layout, outputdata)

def run():
    rospy.init_node('p4b')
    rospy.Subscriber('turtle1/image_sensor', Float64MultiArray, callback)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(20)
    
    message = Twist()
    
    while not rospy.is_shutdown():
        message.linear.x = 1
        message.linear.y = 0
        message.linear.z = 0
        message.angular.x = 0
        message.angular.y = 0
        message.angular.z = math.pi/2
        
        pub.publish(message)
        
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    run()