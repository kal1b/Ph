#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped


def callback(msg):
    pub.publish(msg)


def main():
    rospy.init_node('dsm')
    global pub
    pub = rospy.Publisher('~dsm_state', PoseStamped, queue_size=10)
    rospy.Subscriber('~filtered_state', PoseStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    main()
