import cv2 

img  =  cv2.imread("demo.jpeg" , -1)

img = cv2.resize(img , (800,400))
img = cv2.rotate(img , cv2.cv2.ROTATE_180)

cv2.imshow('Image' , img)



cv2.waitKey(0)
cv2.destroyAllWindows()

