# 이미지에서 텍스트 추출(OCR) 
import cv2
import numpy as np
import pytesseract
import keyboard
import time
import sys
import threading
import serial
import pyautogui 
from skimage.filters import threshold_local # scikit-image
import imutils
from test2 import *

def nothing(x):
    pass

def btn_detect_I2T(arduino): 
    print("start btn_detect")
    while 1:
        if arduino.readable():
            btn = arduino.readline()
            btn = btn.decode()

            if btn[0] == "p":
                print("p")
                pyautogui.press("p")    
                continue 

            if btn[0] == "q":
                print("q")
                sys.exit()

def img_OCR(image):
    cv2.imshow("OCR",image)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(image,lang="Hangul")
    print(text)
    cv2.waitKey(0)
    cv2.destroyWindow("OCR")

def video_cap_I2T():
    x = [0,0,0,0]
    y = [0,0] 
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  
    cv2.namedWindow("video") 
    cv2.createTrackbar('x_1', 'video', x[0], 1000, nothing)
    cv2.createTrackbar('x_2', 'video', x[1], 1000, nothing) 
    cv2.createTrackbar('x_3', 'video', x[2], 1000, nothing)
    cv2.createTrackbar('x_4', 'video', x[3], 1000, nothing)
    cv2.createTrackbar('y_1', 'video', y[0], 1000, nothing)
    cv2.createTrackbar('y_2', 'video', y[1], 1000, nothing)

    while 1:    
        ret, video = cap.read()  

        height, width, channel = video.shape
        matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
        video = cv2.warpAffine(video, matrix, (width, height))
        video_copy = video.copy()
        x_1 = cv2.getTrackbarPos('x_1', 'video')
        x_2 = cv2.getTrackbarPos('x_2', 'video')
        x_3 = cv2.getTrackbarPos('x_3', 'video')
        x_4 = cv2.getTrackbarPos('x_4', 'video')
        y_1 = cv2.getTrackbarPos('y_1', 'video')
        y_2 = cv2.getTrackbarPos('y_2', 'video')

        cv2.circle(video_copy, (x_1, y_1), 5, (0, 0, 255), -1)
        cv2.circle(video_copy, (x_2, y_1), 5, (0, 0, 255), -1)
        cv2.circle(video_copy, (x_3, y_2), 5, (0, 255, 0), -1)
        cv2.circle(video_copy, (x_4, y_2), 5, (0, 255, 0), -1)

        pts1 = np.float32([[x_1, y_1], [x_2, y_1], [x_3, y_2], [x_4, y_2]])
        height, weight = video.shape[:2]
        pts2 = np.float32([[0, 0], [weight, 0], [0, height], [weight, height]])
        mat = cv2.getPerspectiveTransform(pts1, pts2)
        video_result = cv2.warpPerspective(video, mat, (weight, height))

        cv2.imshow('video', video_copy) 
        cv2.imshow('video_result', video_result) 

        k = cv2.waitKey(1) 

        #  "ESC" 입력
        if k == 27:  
            cap.release()
            cv2.destroyAllWindows() 
            break 
        # 이미지 캡쳐 버튼
        elif k == ord('p'):
            img_OCR_th = threading.Thread(target = img_OCR, name=" img_OCR",args = (video_result,))
            img_OCR_th.daemon = True
            img_OCR_th.start()     

    sys.exit()