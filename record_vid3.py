import numpy as np
import cv2

filename1 = 'original.avi'
filename2 = 'compressed.avi'
fps = 24.0

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter( filename1, fourcc, fps, (640,480), 1)
out2 = cv2.VideoWriter( filename2, fourcc, fps, (640,480), 0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out1.write(frame)
    out2.write(gray)
    cv2.imshow('original', frame)
    cv2.imshow('new', gray)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
