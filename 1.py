import numpy as np
import cv2
 
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('original.avi', fourcc, 20.0, (640,  480))
 
 
def rescale_frame(frame, percent = 75):
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent/100)
    height = int(frame.shape[0] * scale_percent/100)
    dim = (width,height)
 
    
 
    return cv2.resize(frame,dim, interpolation=cv2.INTER_AREA)
 
while(True):
    ret, frame = cap.read() #Capture frame by frame
    frame2 = rescale_frame(frame,percent = 30)
 
    out2 = cv2.VideoWriter('compressed.avi', fourcc, 20.0, (frame2.shape[1],  frame2.shape[0]))
 
    out1.write(frame)
    out2.write(frame2)
 
    cv2.imshow('original',frame)
    cv2.imshow('compressed',frame2)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
 
 
cap.release()
cv2.destroyAllWindows()