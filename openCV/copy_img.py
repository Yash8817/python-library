# not working

import cv2

img = cv2.imread('demo.jpeg', -1)
img = cv2.resize(img , (400,400))

tag = img[440:540  ,  220:320]
img[840:940 , 420:520]= tag







cv2.imshow("image" , img)



cv2.waitKey(0)
cv2.destroyAllWindows()
