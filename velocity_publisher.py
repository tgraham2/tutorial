#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Publish this routine to the topic turtle1/cmd_vel，the type of message geometry_msgs::Twist
#
import rospy
from geometry_msgs.msg import Twist

def velocity_publisher():
    # Initialize ROS node
    rospy.init_node('velocity_publisher', anonymous=True)
    # Create a Publishr and pubish a topic named /turtle1/cmd_vel. The type of message is geometry_msgs::Twist and the queue size is 10. 
    turtle_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #set the loop rate
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # Initialize the message of geometry_msgs::Twist type
        vel_msg = Twist()
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.2
        # Publish message
        #
        turtle_vel_pub.publish(vel_msg)
        rospy.loginfo("Publsh turtle velocity command[%0.2f m/s, %0.2f rad/s]", vel_msg.linear.x, vel_msg.angular.z)
        # Delay on the basis of loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass