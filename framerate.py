import cv2
import numpy as np

file1 = 'framerate.avi'
file1_c = 'framerate_compressed.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter(file1, fourcc, 20.0, (640,360))


cap = cv2.VideoCapture(0)

while (True):

    res, frame = cap.read()
    cv2.imshow("Cam",frame)
    out1.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out1.release()
cv2.destroyAllWindows()