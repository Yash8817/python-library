import numpy as np
import cv2


cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()

    # get the height and width of webcam frame
    width = int(cap.get(3)) # .get(3) = 3 get width 
    height  = int(cap.get(4))  # .get(4)  = 4 for  height

    # make blank canvas on 4 frame will be pasted
    img = np.zeros(frame.shape  , np.uint8)

    #make 4 parts
    smaller_frame = cv2.resize(frame , (0,0) , fx=0.5 , fy=0.5)
    
    # paste 4 frame on blank canvas
    img[:height//2 , :width//2]  = cv2.rotate( smaller_frame , cv2.cv2.ROTATE_180) # top left 
    img[height//2: , :width//2]  = smaller_frame    # bottol left
    img[:height//2 , width//2:]  = cv2.rotate( smaller_frame , cv2.cv2.ROTATE_180) # right top
    img[height//2: , :width//2:]  = smaller_frame   # bottom right



    cv2.imshow('press \'s\' to stop' , img)


    if cv2.waitKey(1) == ord('s'):
        break


cap.reliase()
cv2.destroyAllWindows()
