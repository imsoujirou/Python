import cv2
from pyzbar.pyzbar import decode
import time


cam = cv2.VideoCapture(2)
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera == True:
    success, frame = cam.read()
    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(6)
        cv2.imshow("Attendance_QR", frame)
        cv2.waitkey(10000)