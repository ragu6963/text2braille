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
    pts2 = np.float32([[0,0],[1080,0],[0,1920],[1080,1920]])
    mat = cv2.getPerspectiveTransform(pts1,pts2)
    result = cv2.warpPerspective(img,mat,(1080,1920))


    
    cv2.imshow('img', img)
    cv2.imshow('result',result)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()