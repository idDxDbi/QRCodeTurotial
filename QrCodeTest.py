import cv2
import numpy as np
from pyzbar.pyzbar import decode


webcam = True

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 160)



while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread('1.png')

    for barcode in decode(img):
        # print(barcode.data)
        print(barcode)
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon], np.int32)
        # print(pts.shape)
        pts = pts.reshape(-1, 1, 2)
        # print(barcode.rect)
        x, y, w, h =barcode.rect
        # print(x,y,w,h)
        print(pts)
        pts2 = barcode.rect
        # x, y, w, h = barcode.rect
        cv2.putText(img,myData,(pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 3)
        # cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,255), 5)
        cv2.polylines(img, [pts], True,    (255, 0, 255), 5)



    cv2.imshow("Original", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break