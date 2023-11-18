import cv2
import random

img =cv2.imread('python.png',1)
#for i in range(100) :
#    for j in range(img.shape[1]):
#       img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
logo= img[400:900,600:1100] #copy images
img[0:500,0:500]=logo
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


