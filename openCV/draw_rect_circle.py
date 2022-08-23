from typing import ChainMap
import numpy as np
import cv2

cap  =  cv2.VideoCapture(0)

while True:
    ret , frame  = cap.read()

    # draw rectangle
    #                           start point   end point     color  -1=fill else size
    img  = cv2.rectangle(frame , (300,100) , (200,200), (255,0,0) , 5)
    # draw circle
    img  = cv2.circle(img , (200,200) , 50 , (0,0,255) , 5)

    cv2.imshow('webcam' , img)



    if cv2.waitKey(1) == ord('s'):
        break


cap.reliase()
cv2.destroyAllWindows()

