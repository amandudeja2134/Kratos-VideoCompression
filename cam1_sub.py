#!/usr/bin/env python3
import rospy 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
 
def callback(data):
 
  bridge = CvBridge() 
  current_frame = bridge.imgmsg_to_cv2(data)
   
  # Display image
  cv2.imshow("cam1", current_frame)
   
  cv2.waitKey(1)
      
def receive_message():
 
  rospy.init_node('video_sub_py', anonymous=True)
  rospy.Subscriber('video_frame1', Image, callback) # subscriber
  rospy.spin()
  cv2.destroyAllWindows()
  
if __name__ == '__main__':
  receive_message()
