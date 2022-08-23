import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame  = cap.read()


    img  =  cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    cv2.imshow('webcam hsv' , img)
    

    if cv2.waitKey(1) == ord('s'):
        break



cap.reliase()
cv2.destroyAllWindows()