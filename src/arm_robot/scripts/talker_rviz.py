#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header


def talker():
    def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['base_to_mainbase', 'mainbase_to_first', 'first_to_second', 'second_to_thrd', 'left_gripper_joint','right_gripper_joint']
    hello_str.position = [2.14, 2, 2, 0, 0.57, 0.57]
    hello_str.velocity = []
    hello_str.effort = []
    pub.publish(hello_str)
    rate.sleep()

    #while not rospy.is_shutdown():
     ##pub.publish(hello_str)
      #rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

