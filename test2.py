import cv2 
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
while(True):
    ret, img = cap.read()

    cv2.circle(img,(300,50),5,(0,0,255),-1)
    cv2.circle(img,(1500,50),5,(0,0,255),-1)
    cv2.circle(img,(300,900),5,(0,0,255),-1)
    cv2.circle(img,(1500,900),5,(0,0,255),-1)

    pts1 = np.float32([[300,50],[1500,50],[300,900],[1500,900]])
    height,weight = img.shape[:2]
    pts2 = np.float32([[0,0],[weight,0],[0,height],[weight,height]])
    mat = cv2.getPerspectiveTransform(pts1,pts2)
    result = cv2.warpPerspective(img,mat,(weight,height))
    img_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY) 


    
    cv2.imshow('img', img)
    cv2.imshow('result',result)
    cv2.imshow('img_gray',img_gray)

    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()