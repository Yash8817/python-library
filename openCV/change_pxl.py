import cv2
import random

img  = cv2.imread('demo.jpeg' , -1)
img = cv2.resize(img , (400,400))

for  i  in range(200):
    for j in range(img.shape[1]):
        img[j][i] = [random.randint(0,255) , random.randint(0,255)  , random.randint(0,255) ]
        
    





cv2.imshow('Image' , img)

cv2.waitKey(0)

cv2.destroyAllWindows()