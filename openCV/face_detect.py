import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret  ,  frame  = cap.read()
    grey  = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in faces :
        cv2.rectangle(frame , (x,y) , (x+w , y+h),(255,0,0) ,5 )
        roi_gray  = grey[y:y+w , x:x+w]
        roi_color = frame[y:y+h , x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray , 1.3 , 5)
        for (ex,ey,ew,eh) in eyes :
            cv2.rectangle(roi_color , (ex,ey) , (ex+ew , ey+eh),(255,0,0) ,1)



    cv2.imshow("Capture face"  , frame)


    if cv2.waitKey(1) == ord('s'):
        break





cap.release()
cv2.destroyAllWindows()