#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped, Twist


def callback(msg):
    cmd = Twist()
    pub.publish(cmd)


def main():
    rospy.init_node('vfh')
    global pub
    pub = rospy.Publisher('~cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('~dsm_state', PoseStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    main()
