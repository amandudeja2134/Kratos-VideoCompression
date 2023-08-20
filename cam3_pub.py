#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
  
def publish_message():

  pub = rospy.Publisher('video_frame3', Image, queue_size=10)
     
  
  rospy.init_node('video_pub_py', anonymous=True)
     
  rate = rospy.Rate(100)
     
  cam1 = cv2.VideoCapture("/dev/video4")
  cam1.set(3,640)
  cam1.set(4,360)
  
  def resize_frame(frame, width, height):

    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
     
  bridge = CvBridge()
 
  while not rospy.is_shutdown():
     
      
      ret, frame1 = cam1.read()
      frame1_compressed = resize_frame(frame1,640,360)
         
      if ret == True:
        pub.publish(bridge.cv2_to_imgmsg(frame1_compressed))
      rate.sleep()
         
if __name__ == '__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass
