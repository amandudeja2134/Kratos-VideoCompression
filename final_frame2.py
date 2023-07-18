import cv2
import numpy as np

file1 = 'CAM1.avi'
file2 = 'CAM2.avi'

file1_c = 'CAM11_compressed.avi'
file2_c = 'CAM2_compressed.avi'

cam1_id = "/dev/video0"
cam2_id = "/dev/video3"
cam3_id = "/dev/video2"
cam4_id = "/dev/video3"


cam1 = cv2.VideoCapture(cam1_id,cv2.CAP_V4L2)
#cam1.set(3,640)
#cam1.set(4,360)
cam2 = cv2.VideoCapture(cam2_id,cv2.CAP_V4L2)
cam2.set(3,640)
cam2.set(4,360)
cam3 = cv2.VideoCapture(cam3_id,cv2.CAP_V4L2)
cam3.set(3,640)
cam3.set(4,360)
cam4 = cv2.VideoCapture(cam4_id,cv2.CAP_V4L2)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out1 = cv2.VideoWriter(file1_c, fourcc, 20.0, (640,360))
out2 = cv2.VideoWriter(file2_c, fourcc, 20.0, (640,360))
#out3 = cv2.VideoWriter(file3_c, fourcc, 20.0, (640,360))
#out4 = cv2.VideoWriter(file4_c, fourcc, 20.0, (640,360))

def resize_frame(frame, width, height):

    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

while (True):
    ret, frame1 = cam1.read()
    frame1_c = resize_frame(frame1,640,360)
    out1.write(frame1_c)
    cv2.imshow('compresssed',frame1_c)

    #ret, frame2 = cam2.read()
    #frame2_c = resize_frame(frame2, 640,360)
    #out2.write(frame2_c)
    #cv2.imshow('cam2',frame2_c)

    ret, frame3 = cam3.read()
    #frame3_c = resize_frame(frame3, 640,360)
    #out3.write(frame3_c)
    #cv2.imshow('cam3',frame3_c)

    ret, frame4 = cam4.read()
    #frame4_c = resize_frame(frame4, 640,360)
    #out4.write(frame4_c)
    #cv2.imshow('cam4',frame4_c)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam1.release()
cam2.release()
cam3.release()
cam4.release()
out1.release()
out2.release()
cv2.destroyAllWindows()