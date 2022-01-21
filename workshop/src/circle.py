#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    while not rospy.is_shutdown():
        rospy.init_node("circle")
        pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        vel = Twist()
        #v=rw
        radius = 2

        vel.linear.x = 0.25
        vel.angular.z = 0.25/radius
        pub.publish(vel)