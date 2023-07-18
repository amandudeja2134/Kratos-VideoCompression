import cv2
import numpy as np

def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)

def make_720p():
    cap.set(3,1280)
    cap.set(4,720)

def make_480p():
    cap.set(3,640)
    cap.set(4,480)


def resize_frame(frame, percent):
    width = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

cap = cv2.VideoCapture(0)

print ("camera connection complete..")

file1 = 'original.avi'
file2 = 'compressed_480p.avi'
#file3 = 'compressed_360p.avi'
fps = 24.0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out3 = cv2.VideoWriter(file3, fourcc, fps, (640,360), 1)
out2 = cv2.VideoWriter(file2, fourcc, fps, (640,480), 1)
out1 = cv2.VideoWriter(file1, fourcc, fps, (1280,720), 1)
while True:
    ret, frame = cap.read()
    frame1 = resize_frame(frame, 100)
    frame2 = resize_frame(frame, 50)
    #frame3 = resize_frame(frame, 25)
    out1.write(frame1)
    out2.write(frame2)
    #out3.write(frame3)
    cv2.imshow('original', frame1)
    cv2.imshow('compressed_480p', frame2)
    #cv2.imshow('compressed_360p', frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out1.release()
out2.release()
#out3.release()
cv2.destroyAllWindows()