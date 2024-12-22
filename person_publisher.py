#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#This routine will pulish /person_info topic and customize message type beginner_hiwonder::Person

import rospy
from beginner_hiwonder.msg import Person

def velocity_publisher():
  # Initialize ROS node
  rospy.init_node('person_publisher', anonymous=True)
  # Create a publisher and publish a topic named /person_info. The message type is
  # beginner_hiwonder::Person and the queue length is 10.

  person_info_pub = rospy.Publisher('/person_info', Person, queue_size=10)
  #set the loop rate
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():
    # Initialize the message of beginner_hiwonder::Person type
    person_msg = Person()
    person_msg.name = "Tom";
    person_msg.age = 18;
    person_msg.sex = Person.male;

    # publish message
    person_info_pub.publish(person_msg)
    rospy.loginfo("Publsh person message[%s, %d, %d]", person_msg.name, person_msg.age, person_msg.sex)

    # Delay on basis of the loop rate
    rate.sleep()

if __name__ == '__main__':
  try:
    velocity_publisher()
  except rospy.ROSInterruptException:
    pass
