import cv2
import numpy as np
import pytesseract
import keyboard
import time
import sys
import threading
import serial
import pyautogui

def nothing(x):
    pass

def btn_detect():
    print("start btn_detect")
    while(1):
        if arduino.readable():
            wait = arduino.readline()
            wait = wait.decode()
            if wait[0] == "p":
                print("p")
                pyautogui.press("p")    
                continue
            if wait[0] == "q":
                print("q")
                sys.exit(0)   
    
def OCR(image):
    cv2.imshow("OCR",image)
    cv2.waitKey(0)
    cv2.destroyWindow("OCR")


def video(): 
    x_1 = 0
    x_2 = 0
    x_3 = 0
    x_4 = 0
    y_1 = 0
    y_2 = 0  
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  
    cv2.namedWindow("img") 
    cv2.createTrackbar('x_1', 'img', x_1, 1000, nothing)
    cv2.createTrackbar('x_2', 'img', x_2, 1000, nothing) 
    cv2.createTrackbar('x_3', 'img', x_3, 1000, nothing)
    cv2.createTrackbar('x_4', 'img', x_4, 1000, nothing)
    cv2.createTrackbar('y_1', 'img', y_1, 1000, nothing)
    cv2.createTrackbar('y_2', 'img', y_2, 1000, nothing)

    while True:    
        ret, img = cap.read()  

        height, width, channel = img.shape
        matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
        img = cv2.warpAffine(img, matrix, (width, height))
        copy = img.copy()
        x_1 = cv2.getTrackbarPos('x_1', 'img')
        x_2 = cv2.getTrackbarPos('x_2', 'img')
        x_3 = cv2.getTrackbarPos('x_3', 'img')
        x_4 = cv2.getTrackbarPos('x_4', 'img')
        y_1 = cv2.getTrackbarPos('y_1', 'img')
        y_2 = cv2.getTrackbarPos('y_2', 'img')

        cv2.circle(copy, (x_1, y_1), 5, (0, 0, 255), -1)
        cv2.circle(copy, (x_2, y_1), 5, (0, 0, 255), -1)
        cv2.circle(copy, (x_3, y_2), 5, (0, 255, 0), -1)
        cv2.circle(copy, (x_4, y_2), 5, (0, 255, 0), -1)

        pts1 = np.float32([[x_1, y_1], [x_2, y_1], [x_3, y_2], [x_4, y_2]])
        height, weight = img.shape[:2]
        pts2 = np.float32([[0, 0], [weight, 0], [0, height], [weight, height]])
        mat = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(img, mat, (weight, height))

        cv2.imshow('img', copy) 
        cv2.imshow('result', result) 
        
        k = cv2.waitKey(1) 

        if k == 27:  
            cap.release()
            cv2.destroyAllWindows()
            break 

        elif k == ord('p'):
            th3 = threading.Thread(target = OCR, name="OCR",args = (result,))
            th3.start()   

arduino = serial.Serial("COM5", 9600)

th1 = threading.Thread(target = btn_detect, name="btn_detect")
th1.start()

th2 = threading.Thread(target = video, name="video")
th2.start() 