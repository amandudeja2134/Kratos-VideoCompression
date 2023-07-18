import cv2
from datetime import datetime

def gstreamer_pipeline(capture_width=640, capture_height=360, display_width=640, display_height=360, framerate=30):

    return f'v4l2src device=/dev/video0 ! video/x-raw, width=(int){capture_width}, height=(int){capture_height}, format=(string)YUY2, framerate=(fraction){framerate}/1 ! videoconvert ! video/x-raw, width=(int){display_width}, height=(int){display_height}, format=(string)RGB ! videoconvert ! appsink'


cam = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

while True:
    ret, frame = cam.read()
    print(frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()