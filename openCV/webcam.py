import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame  = cap.read()


    
    cv2.imshow('webcam hsv' , frame)
    

    if cv2.waitKey(1) == ord('s'):
        break



cap.reliase()
cv2.destroyAllWindows()