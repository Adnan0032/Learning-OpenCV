import cv2
import numpy as np

cap=cv2.VideoCapture(0) #create capture video

while True:
    ret,frame =cap.read() #read the capture and put it in a frame
    width=int(cap.get(3))
    height=int(cap.get(4))

    image=np.zeros(frame.shape,np.uint8) #make the image black
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5) #resize the image to half
    image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:,:width//2]=smaller_frame
    image[:height//2,width//2:]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:,width//2:]=smaller_frame

    cv2.imshow('frame',image) #show the frame


    if cv2.waitKey(1)== ord('q'): #when we press q we exit the frame
        break
cap.release() 
cv2.destroyAllWindows()