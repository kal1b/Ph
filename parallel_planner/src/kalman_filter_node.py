#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped


def callback(msg):
    pub.publish(msg)


def main():
    rospy.init_node('kalman_filter')
    global pub
    pub = rospy.Publisher('~filtered_state', PoseStamped, queue_size=10)
    rospy.Subscriber('~input_state', PoseStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    main()
