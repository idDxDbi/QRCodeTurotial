import cv2
import numpy as np
import math
import time
from pyzbar.pyzbar import decode





webcam = False
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()

print(myDataList)



while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread('img.png')


    for barcode in decode(img):
        print(barcode)
        # mydata = barcode.data
        mydata = str(barcode.data.decode('utf-8'))
        # mydata = barcode.data.decode('utf-8')

        if mydata in myDataList:
            print("Authorized")
            result = 'Authorized'
            color = (0,255,0)
        else:
            print("Un-Authorized")
            result = 'Un-Authorized'
            color = (0, 0, 255)

        pts = np.array((barcode.polygon),np.int32)
        pts2 = barcode.rect
        # print(pts)
        print(pts2)
        cv2.polylines(img, [pts], True, color,5)
        # cv2.putText(img, mydata+" "+result, (pts2[0]-10,pts2[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.putText(img, mydata+" "+result, (pts2[0], pts2[1]+(int(pts2[3]/2))), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # print(mydata)








    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break