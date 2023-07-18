import numpy as np
import cv2
import os


filename1 = 'video1.avi'
filename2 = 'video2.avi'
frames_per_second = 15.0
my_res1 = '480p'
my_res2 = '720p'

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

def get_dims(cap, res):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)
dims1 = get_dims(cap, res=my_res1)
dims2 = get_dims(cap, res=my_res2)
video_type_cv2 = get_video_type(filename1)

out2 = cv2.VideoWriter(filename1, video_type_cv2, frames_per_second, dims2, 0)
out1 = cv2.VideoWriter(filename2, video_type_cv2, frames_per_second, dims1, 0)


while True:
    ret, frame = cap.read()
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out1.write(frame)
    out2.write(frame1)
    cv2.imshow('frame1', frame)
    cv2.imshow('frame2', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows