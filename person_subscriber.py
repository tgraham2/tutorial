#!/usr/bin/env python
# -*- coding: utf-8 -*- # This routine will subscribe to the /person_info topic and customize the message type
beginner_hiwonder::Person

import rospy
from beginner_hiwonder.msg import Person

def personInfoCallback(msg):
 rospy.loginfo("Subcribe Person Info: name:%s age:%d sex:%d", msg.name, msg.age, msg.sex)

def person_subscriber():
  # Initialize ROS node
  rospy.init_node('person_subscriber', anonymous=True)

# Create a subscriber, subsribe the topic named /person_info and register the callback
funcation personInfoCallback
  rospy.Subscriber("/person_info", Person, personInfoCallback)

  # loop and wait the callback function
  rospy.spin()

if __name__ == '__main__':
  person_subscriber()
