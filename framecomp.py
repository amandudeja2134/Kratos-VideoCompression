import cv2
import numpy as np

file1 = "frame_o.avi"
file2 = "frame_c.avi"
fps = 5

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter( file2, fourcc, fps, (640,360))

cam = cv2.VideoCapture(0)

def resize_frame(frame, width, height):

    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

while (True):
    ret, frame = cap.read()
    frame1 = resize_frame(frame,640,360)
    out1.write(frame1)
    cv2.imshow('original', frame1)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

cap.release()
out1.release()
cv2.destroyAllWindows()