import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'divx')
while True:
    ret,frame=cap.read()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640,480)
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
