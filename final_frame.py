import cv2
import numpy as np

cam1_id = "/dev/video0"
cam2_id = "/dev/video2"
cam3_id = "/dev/video3"
cam4_id = "/dev/video3"


cam1 = cv2.VideoCapture(cam1_id,cv2.CAP_V4L2)
cam1.set(3,640)
cam1.set(4,480)
cam2 = cv2.VideoCapture(cam2_id,cv2.CAP_V4L2)
cam2.set(3,256)
cam2.set(4,144)
cam3 = cv2.VideoCapture(cam3_id,cv2.CAP_V4L2)
cam3.set(3,640)
cam3.set(4,360)
cam4 = cv2.VideoCapture(cam4_id,cv2.CAP_V4L2)

def resize_frame(frame, width, height):

    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

while (True):
    ret, frame1 = cam1.read()
    #frame1_c = resize_frame(frame1,640,360)
    #cv2.imshow('original', frame1)

    ret, frame2 = cam2.read()
    #frame2_c = resize_frame(frame2, 640,360)
    cv2.imshow('cam2',frame2)

    ret, frame3 = cam3.read()
    frame3_c = resize_frame(frame3, 640,360)
    cv2.imshow('cam3',frame3_c)

    ret, frame4 = cam4.read()
    #frame4_c = resize_frame(frame4, 640,360)
    #cv2.imshow('cam4',frame4_c)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam1.release()
cam2.release()
cam3.release()
cam4.release()
cv2.destroyAllWindows()