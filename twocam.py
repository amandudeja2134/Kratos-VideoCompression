import numpy as np
import cv2

flip=2
dispW=320
dispH=240
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam1 = cv2.VideoCapture(camSet)

fps = 24.0

cam2 = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

while(True):
    ret, frame2 = cam2.read()
    cv2.imshow('original', frame2)

    ret, frame1 = cam1.read()
    cv2.imshow('original', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam1.release()
cam2.release()
cv2.destroyAllWindows()
