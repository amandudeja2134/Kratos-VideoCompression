import cv2

file1 = 'original.avi'
file2 = 'compressed1.avi'
file3 = 'compressed2.avi'
cap = cv2.VideoCapture("/dev/video0",cv2.CAP_V4L2)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter(file1, fourcc, 20.0, (1280,720))
out2 = cv2.VideoWriter(file2, fourcc, 20.0, (640,480))
out3 = cv2.VideoWriter(file3, fourcc, 20.0, (640,360))

def resize_frame(frame, width, height):

    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


while(True):
    ret, frame = cap.read()
    frame1 = resize_frame(frame, 1280,720)
    out1.write(frame1)
    cv2.imshow('original', frame1)
    frame2 = resize_frame(frame, 640, 480)
    out2.write(frame2)
    cv2.imshow('compressed1', frame2)
    frame3 = resize_frame(frame, 640,360)
    out3.write(frame3)
    cv2.imshow('compressed2', frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out1.release()
out2.release()
out3.release()
cv2.destroyAllWindows()