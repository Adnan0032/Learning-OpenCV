import cv2
import numpy as np

cap=cv2.VideoCapture(0) #create capture video

while True:
    ret,frame =cap.read() #read the capture and put it in a frame
    width=int(cap.get(3))
    height=int(cap.get(4))
    img =cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    img2=cv2.line(img,(width,0),(0,height),(0,0,255),10)
    img3=cv2.rectangle(img,(100,100),(200,200),(128,128,128),5)
    img4=cv2.circle(img,(300,300),60,(0,255,0),-1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    img4=cv2.putText(img,'Adnane is here',(10,height-10),font,1,(0,0,0),5,cv2.LINE_AA)
    cv2.imshow('frame',img3) #show the frame


    if cv2.waitKey(1)== ord('q'): #when we press q we exit the frame
        break
cap.release() 
cv2.destroyAllWindows()
