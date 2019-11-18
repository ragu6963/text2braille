import cv2
import numpy as np
import pytesseract
import keyboard
import time

def nothing(x):
    pass

x_1 = 0
x_2 = 0
x_3 = 0
x_4 = 0
y_1 = 0
y_2 = 0 

while(True): 
    cap = cv2.VideoCapture(0)  
    cv2.namedWindow("img") 
    cv2.createTrackbar('x_1', 'img', x_1, 1000, nothing)
    cv2.createTrackbar('x_2', 'img', x_2, 1000, nothing) 
    cv2.createTrackbar('x_3', 'img', x_3, 1000, nothing)
    cv2.createTrackbar('x_4', 'img', x_4, 1000, nothing)
    cv2.createTrackbar('y_1', 'img', y_1, 1000, nothing)
    cv2.createTrackbar('y_2', 'img', y_2, 1000, nothing)
    while(True):    
        ret, img = cap.read()  
        height, width, channel = img.shape
        matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
        img = cv2.warpAffine(img, matrix, (width, height))
        x_1 = cv2.getTrackbarPos('x_1', 'img')
        x_2 = cv2.getTrackbarPos('x_2', 'img')
        x_3 = cv2.getTrackbarPos('x_3', 'img')
        x_4 = cv2.getTrackbarPos('x_4', 'img')
        y_1 = cv2.getTrackbarPos('y_1', 'img')
        y_2 = cv2.getTrackbarPos('y_2', 'img')
        cv2.circle(img, (x_1, y_1), 5, (0, 0, 255), -1)
        cv2.circle(img, (x_2, y_1), 5, (0, 0, 255), -1)
        cv2.circle(img, (x_3, y_2), 5, (0, 255, 0), -1)
        cv2.circle(img, (x_4, y_2), 5, (0, 255, 0), -1)
        pts1 = np.float32([[x_1, y_1], [x_2, y_1], [x_3, y_2], [x_4, y_2]])
        height, weight = img.shape[:2]
        pts2 = np.float32([[0, 0], [weight, 0], [0, height], [weight, height]])
        mat = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(img, mat, (weight, height))
        cv2.imshow('img', img) 
        cv2.imshow('result', result)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break  
    cap.release()
    cv2.destroyAllWindows() 
    print("...")
    while 1:    
        if keyboard.is_pressed('q'):
            time.sleep(0.1)
            break
