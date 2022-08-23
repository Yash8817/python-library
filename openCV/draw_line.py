import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    ret  , frame  =  cap.read()
    width  =  int(cap.get(3))
    height  =  int(cap.get(4))

    img  =  cv2.line(frame , (0,0) , (width , height) , (255,0,0), 5)
    img  =  cv2.line(img , (0,height) , (width ,0) , (0,255,0), 3)


    cv2.imshow('press \'s\' to stop' , img)
    if cv2.waitKey(1) == ord('s'):
        break


cap.reliase()
cv2.destroyAllWindows()
