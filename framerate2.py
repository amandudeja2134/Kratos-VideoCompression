import cv2
import numpy as np
import time

frame_rate = 10
prev = 0


cap = cv2.VideoCapture(0)

while (True):

    time_elapsed = time.time() - prev
    res, frame = cap.read()

    if time_elapsed > 1./frame_rate:
        prev = time.time()

    cv2.imshow("Cam",frame)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()