#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    while not rospy.is_shutdown():
        rospy.init_node("publisher")
        pub = rospy.Publisher("chatter", String, queue_size=10)
        string = String()
        string.data = "Hello World!"
        pub.publish(string)

        rate = rospy.Rate(1)
        rate.sleep()