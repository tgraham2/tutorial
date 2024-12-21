#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from turtlesim.msg import Pose

def poseCallback(msg):
    rospy.loginfo("Turtle pose: x:%0.6f, y:%0.6f", msg.x, msg.y)

def pose_subscriber():
    # Initialize ROS node
    rospy.init_node('pose_subscriber', anonymous=True)
    # Create a subsriber, subscribe to the topic named
    # /turtle1/pose and register callback function poseCallback
    rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
    # Loop and wait callback function
    rospy.spin()

if __name__ == '__main__':
    pose_subscriber()