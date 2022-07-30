import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(5,720)
cap.set(4,480)
with open('mydata.text') as f:
    mydatalist=f.read().splitlines()
while True:
    success,img=cap.read()
    for barcode in decode(img):
        mydata=barcode.data.decode('utf-8')
        print(mydata)
        if mydata in mydatalist:
            myoutput = 'Authorized'
            mycolour = (0, 255, 0)
        else:
            myoutput = 'Un-authorized'
            mycolour = (0, 0, 255)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,mycolour,5)
        pts2=barcode.rect
        cv2.putText(img, mydata, (pts2[0], pts2[1] - 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, mycolour, 2)
        cv2.putText(img, myoutput, (pts2[0], pts2[1] - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, mycolour, 2)
    cv2.imshow('result',img)
    cv2.waitKey(1)