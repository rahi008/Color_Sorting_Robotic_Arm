#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import time

def talker():
    
    pub=rospy.Publisher("/joint_states", JointState, queue_size=10)    
    rospy.init_node('joint_state_publisher')    
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    
    hello_str.name = ['base_to_mainbase', 'mainbase_to_first', 'first_to_second', 'second_to_third', 'left_gripper_joint']
    hello_str.position = [2.30, 1.41, 2.44, 1.15, 0]
    hello_str.velocity = []
    hello_str.effort = []
    
    a=1;
    while not a==2:
        hello_str.position = [2.30, 0.86, 2.44, 1.15, 0.55]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1
    
    time.sleep(3)
    a=1;
    while not a==2:
        hello_str.position = [2.30, 0.86, 2.44, 1.15, 0]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1     


    time.sleep(3)
    a=1;
    while not a==2:
        hello_str.position = [2.30, 1.41, 2.44, 1.15, 0]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1  


    time.sleep(3)
    a=1;
    while not a==2:
        hello_str.position = [1.52, 1.41, 2.44, 1.15, 0]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1     


    time.sleep(3)
    a=1;
    while not a==2:
        hello_str.position = [1.52, 0.86, 2.44, 1.15, 0]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1    


    time.sleep(3)
    a=1;
    while not a==2:
        hello_str.position = [1.52, 0.86, 2.44, 1.15, 0.55]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1
    

    time.sleep(3)
    a=1;
    while not a==2:
        hello_str.position = [1.52, 1.41, 2.44, 1.15, 0.55]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1
    
    
    time.sleep(3)
    a=1;
    while not a==2:
        hello_str.position = [2.30, 1.41, 2.44, 1.15, 0.55]
        hello_str.header.stamp = rospy.Time.now() 
        rospy.loginfo(hello_str)   	
        pub.publish(hello_str)
        rate.sleep()
        time.sleep(5)
        a+=1

                          

    #
     ##pub.publish(hello_str)
      #rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

  
