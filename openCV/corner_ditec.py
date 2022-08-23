import numpy as np
import cv2

img  = cv2.imread('chess.jpg')

img = cv2.resize(img , (0,0) , fx=0.5 , fy= 0.5) 

# convert to gray scel
grey  = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
corners  = cv2.goodFeaturesToTrack(grey,25,0.01,10)

# convert to int 
corners = np.int0(corners)

for i  in corners:
    x,y  = i.reval()
    cv2.circle(img , (x,y) ,5 ,(255,0,0) ,5 )

    


cv2.imshow('Image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()