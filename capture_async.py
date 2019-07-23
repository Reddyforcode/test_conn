import cv2
from videocaptureasync import *

#vid = cv2.VideoCapture('rtsp://administrator:@172.16.20.98/defaultPrimary?streamType=u')
#vid = cv2.VideoCapture('rtsp://admin:admin@172.16.20.11/defaultPrimary?streamType=u')

video_capture = VideoCaptureAsync()
video_capture.start()
while True:

    _, img = video_capture.read()
    print(type(img))
    cv2.imshow('hoolo', img)
    #cv2.imwrite("works.jpg", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.stop()
