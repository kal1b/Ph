#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class PlannerNode(object):
    def __init__(self):
        self.cmd_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel', Twist, queue_size=10)
        self.state_pub = rospy.Publisher('state', String, queue_size=10)
        neighbors = rospy.get_param('~neighbors', [])
        for n in neighbors:
            rospy.Subscriber(n, String, self.neighbor_cb)
        rospy.Subscriber('~cmd_vel', Twist, self.cmd_cb)
        rospy.Timer(rospy.Duration(1.0), self.state_timer)

    def cmd_cb(self, msg):
        self.cmd_pub.publish(msg)

    def neighbor_cb(self, msg):
        pass

    def state_timer(self, event):
        msg = String()
        msg.data = 'ok'
        self.state_pub.publish(msg)


def main():
    rospy.init_node('parallel_planner_node')
    PlannerNode()
    rospy.spin()


if __name__ == '__main__':
    main()
