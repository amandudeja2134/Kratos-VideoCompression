import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)

def make_720p():
    cap.set(3,1280)
    cap.set(4,720)

def make_480p():
    cap.set(3,640)
    cap.set(4,480)

def make_custom(width,height):
    cap.set(3,width)
    cap.set(4,height)

def resize_frame(frame, percent):
    width = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()
    frame1 = resize_frame( frame, 30)
    cv2.imshow('frame1', frame1)
    frame2 = resize_frame( frame, 70)
    cv2.imshow('frame2', frame2)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
