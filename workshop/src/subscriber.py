#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    message = data.data
    print(message)

if __name__ == "__main__":
    rospy.init_node("subscriber")
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()