import numpy as np
import cv2

filename1 = 'original_720p.avi'
filename2 = 'compressed_480p.avi'
fps = 2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter( filename1, fourcc, fps, (1280,720))
out2 = cv2.VideoWriter( filename2, fourcc, fps, (640,480))

def resize_frame(frame, width, height):

    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


while(True):
    ret, frame = cap.read()
    frame1 = resize_frame(frame,1280,720)
    frame2 = resize_frame(frame, 640,480)
    out1.write(frame1)
    out2.write(frame2)
    cv2.imshow('original', frame1)
    cv2.imshow('compressed', frame2)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
