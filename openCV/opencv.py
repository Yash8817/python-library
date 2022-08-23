import cv2

img = cv2.imread('demo.jpeg',-1)

img = cv2.resize(img , (800,400))
cv2.imshow('Image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()