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

src = [] 

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
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    GaussianBlur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("GaussianBlur",GaussianBlur)

    # bilateralFilter = cv2.bilateralFilter(gray,5,75,75)
    # cv2.imshow("bilateralFilter",bilateralFilter)

    th1 = cv2.adaptiveThreshold(GaussianBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    # th2 = cv2.adaptiveThreshold(bilateralFilter,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imshow("th1",th1)
    # cv2.imshow("th2",th2)

    # ret2, th3 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    kernel = np.ones((1, 1), np.uint8)
    dilate1 = cv2.erode(th1, kernel, iterations = 1)
    # dilate2 = cv2.erode(th2, kernel, iterations = 1)

    cv2.imshow("dilate1",dilate1)
    # cv2.imshow("dilate2",dilate2)

    # cv2.imshow("th2",th2)

    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(dilate1,config=config)
    print(text)
    # text = pytesseract.image_to_string(dilate2,config=config)
    # print(text)
    cv2.waitKey(0)   
    cv2.destroyWindow("dilate1")
    # cv2.destroyWindow("dilate2")

def mouse_handler(event, x, y, flags, param):
    global src 
    if event == cv2.EVENT_LBUTTONUP:
        src.append([x, y]) 
    if event == cv2.EVENT_RBUTTONUP:
        src = []
        cv2.destroyWindow("result")

def video_cap_I2T(): 
    global src
    cv2.namedWindow('video')
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  

    while 1:    
        ret, video = cap.read()  
        cv2.setMouseCallback('video', mouse_handler,video)

        height, width, channel = video.shape
        matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
        video = cv2.warpAffine(video, matrix, (width, height))
        video = cv2.resize(video, (2*width, 2*height), interpolation = cv2.INTER_CUBIC )
        
        video_copy = video.copy()

        for xx,yy in src:
            cv2.circle(video_copy,center=(xx, yy), radius=5, color=(0, 255, 0), thickness=-1, lineType=cv2.LINE_AA)

        cv2.imshow('video', video_copy) 

        if len(src) == 4:
            src_np = np.array(src, dtype=np.float32)
            width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
            height = max(np.linalg.norm(src_np[0] - src_np[3]), np.linalg.norm(src_np[1] - src_np[2]))
            dst_np = np.array([[0, 0],[width, 0],[width, height],[0, height]], dtype=np.float32)
            M = cv2.getPerspectiveTransform(src=src_np, dst=dst_np)
            result = cv2.warpPerspective(video, M=M, dsize=(width, height))
            height, width = result.shape[:2]
            # result = cv2.resize(result, (2*width, 2*height), interpolation = cv2.INTER_CUBIC )
            cv2.imshow('result', result)   

        k = cv2.waitKey(1) 
        #  "ESC" 입력
        if k == 27:  
            cap.release()
            cv2.destroyAllWindows() 
            break 
        # 이미지 캡쳐 버튼
        elif k == ord('p'):
            if len(src) == 4:
                img_OCR_th = threading.Thread(target = img_OCR, name="img_OCR",args = (result,))
                img_OCR_th.daemon = True
                img_OCR_th.start()     
    sys.exit()