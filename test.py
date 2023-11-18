import cv2

img =cv2.imread('python.png',1)
img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new.png',img)
cv2.imshow('Python',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


