#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from jointstate_to_plain.msg import Dofs


def cb(msg):
    rospy.loginfo("Position: %s", str(msg.position))
    dofs = Dofs() 
    dofs.claws = (int) (msg.position[4]*255/0.55)
    dofs.s_to_thrd = (int) (msg.position[3]*180/3.14)
    dofs.f_to_s = (int) (msg.position[2]*180/3.14)
    dofs.bs_to_f = (int) (msg.position[1] * 180/3.14)
    dofs.base = (int) (msg.position[0] * 180/3.14)
  
    pub.publish(dofs)
    
    
    


 

if __name__ == '__main__':
 
    rospy.init_node('jointstate_to_plain')
    pub=rospy.Publisher("/arm_dofs", Dofs, queue_size=1)
   
    rospy.Subscriber("joint_states", JointState, cb)
    

    rospy.spin()
