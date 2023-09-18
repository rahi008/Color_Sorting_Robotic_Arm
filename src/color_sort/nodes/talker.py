#!/usr/bin/env python
import rospy
import cv2
import numpy as np
import time
from std_msgs.msg import UInt16
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import time
def talker():
             #pub = rospy.Publisher('/servo', UInt16, queue_size=1)
             pub=rospy.Publisher("/joint_states", JointState, queue_size=10)
             #rospy.init_node('talker',anonymous=True)
             rospy.init_node('joint_state_publisher')
             rate=rospy.Rate(10)
	     cap = cv2.VideoCapture(1)

	     while not rospy.is_shutdown():
                           
                           cr=0
                           cb=0
                           cg=0
                           ret,im = cap.read() #READ FRAMES
                           hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) #CONVERT FRAMES FROM COLOR TO HSV
                           #lower mask red
                           #lower_red = np.array([0,100,100])
                           #upper_red = np.array([10,255,255])
                           #mask0 = cv2.inRange(hsv, lower_red ,upper_red)
                           #upper mask red
                           #lower_red = np.array([150,100,100])
                           #upper_red = np.array([179,255,255])
                           #mask1 = cv2.inRange(hsv, lower_red ,upper_red)
                           #mask=mask0
                           #yellow
                           #lowyellow=np.array([20,50,100],dtype=np.uint8)
                           #highyellow=np.array([42,255,255],dtype=np.uint8)
                           #mask = cv2.inRange(hsv, lowyellow,highyellow)
                           #blue
                           lowblue=np.array([110,130,50],dtype=np.uint8)
                           highblue=np.array([130,255,255],dtype=np.uint8)
                           maskb = cv2.inRange(hsv, lowblue,highblue)
                           #green
                           lowgreen=np.array([44,54,63],dtype=np.uint8)
                           highgreen=np.array([90,255,255],dtype=np.uint8)
                           maskg = cv2.inRange(hsv, lowgreen,highgreen)
                           #cr=cv2.countNonZero(mask)
                           cb=cv2.countNonZero(maskb)
                           rospy.loginfo(cb)
                           cg=cv2.countNonZero(maskg)
                           hello_str = JointState()
                           hello_str.header = Header()
                               
                           hello_str.name = ['base_to_mainbase','mainbase_to_first', 'first_to_second', 'second_to_third', 'left_gripper_joint']
                           hello_str.velocity = []
                           hello_str.effort = []
                           if(cb>4000):
                               print 'blue'
			       cb=0
                               
                               #a=5;
                               #hello_str = " %d" % rospy.get_time()
                               #rospy.loginfo(a)
                               #pub.publish(a)
                               #time.sleep(1) 
                               
                               
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 0.86, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
    
                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 0.86, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1     


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 1.41, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1  


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [3.14, 1.41, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1     


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [3.14, 0.86, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1    


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [3.14, 0.86, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
    

                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [3.14, 1.41, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
    
    
                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 1.41, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
                               time.sleep(8)
                           elif(cg>4000):
                               print 'green'
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 0.86, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
    
                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 0.86, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1     


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 1.41, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1  


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [1.52, 1.41, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1     


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [1.52, 0.86, 2.44, 1.15, 0]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1    


                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [1.52, 0.86, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
    

                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [1.52, 1.41, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
    
    
                               time.sleep(2)
                               a=1;
                               while not a==2:
                                   hello_str.position = [2.30, 1.41, 2.44, 1.15, 0.55]
                                   hello_str.header.stamp = rospy.Time.now() 
                                   rospy.loginfo(hello_str)   	
                                   pub.publish(hello_str)
                                   rate.sleep()
                                   time.sleep(5)
                                   a+=1
                           cb=0
                           cg=0
                           
                       

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
cap.release()
cv2.destroyAllWindows()
