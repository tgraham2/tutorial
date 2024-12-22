#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This routine will request /spawn service and the service data type is turtlesim::Spawn

import sys
import rospy

from turtlesim.srv import Spawn

def turtle_spawn():
    # Initialize ROS node
    rospy.init_node('turtle_spawn')

    # After finding the /spawn service, create a service client, and then connect the service named /spawn. 
    rospy.wait_for_service('/spawn')
    try:
        add_turtle = rospy.ServiceProxy('/spawn', Spawn)

        # Request service call and input request data
        response = add_turtle(2.0, 2.0, 0.0, "turtle2")
        return response.name
    
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    #The service calls and displays the result of call. 
    print "Spwan turtle successfully [name:%s]" %(turtle_spawn())
