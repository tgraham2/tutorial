#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# This routine set and read the parameter in turtle routine

import sys
import rospy
from std_srvs.srv import Empty

def parameter_config():
    # Initialize ROS node
    rospy.init_node('parameter_config', anonymous=True)

    # read the parameter of blackground color
    red = rospy.get_param('/turtlesim/background_r')
    green = rospy.get_param('/turtlesim/background_g')
    blue = rospy.get_param('/turtlesim/background_b')

    rospy.loginfo("Get Backgroud Color[%d, %d, %d]", red, green, blue)

    # set the parameter of blackground color
    rospy.set_param("/turtlesim/background_r", 255);
    rospy.set_param("/turtlesim/background_g", 255);
    rospy.set_param("/turtlesim/background_b", 255);

    rospy.loginfo("Set Backgroud Color[255, 255, 255]");

    # read the parameter of blackground color
    red = rospy.get_param('/turtlesim/background_r')
    green = rospy.get_param('/turtlesim/background_g')
    blue = rospy.get_param('/turtlesim/background_b')

    rospy.loginfo("Get Backgroud Color[%d, %d, %d]", red, green, blue)

    # After finding /spawn, create a service client, and then connect service named /spawn. 
    rospy.wait_for_service('/clear')
    try:
        clear_background = rospy.ServiceProxy('/clear', Empty)

        # Request service call, enter request data
        response = clear_background()
        return response

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    parameter_config()
