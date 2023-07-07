import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()

    if not success:
        break

    for code in decode(img):
        decoded_data = code.data.decode('utf-8')
        rect_pts = code.rect

        if decoded_data:
            pts = np.array([code.polygon], np.int32)
            cv2.polylines(img, [pts], True, (255, 0, 0), 3)
            print(code.data.decode('utf-8'))

    cv2.imshow("QR_Code Scanner", img)
    cv2.waitKey(1)

cap.release()