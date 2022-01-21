#!/usr/bin/env python3 

import rospy

if __name__ == "__main__":
    while not rospy.is_shutdown():
        rospy.init_node("node")
        rate = rospy.Rate(1)
        print("Node is active")
        rate.sleep()
    print("Shutting down")