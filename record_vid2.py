import numpy as np
import cv2

filename = 'output.avi'
fps = 24.0

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter( filename, fourcc, fps, (640,480), 0)

while(True):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('original', frame)
    #cv2.imshow('new', gray)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
