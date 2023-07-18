import cv2

file1 = 'original.avi'
file2 = 'compressed1.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter(file1, fourcc, 20.0, (1280,720))
out2 = cv2.VideoWriter(file2, fourcc, 20.0, (640,480))
flip=2
dispW=320
dispH=240

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap0 = cv2.VideoCapture(camSet)


def resize_frame(frame, width, height):

    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


while(True):
    ret0, frame0 = cap0.read()
    frame1 = resize_frame(frame0, 1280,720)
    cv2.imshow('cam1',frame1)
    out1.write(frame1)
    frame2 = resize_frame(frame0, 640, 480)
    out2.write(frame2)
    cv2.imshow(frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cv2.destroyAllWindows()