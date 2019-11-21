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
from Text2Braille import * 

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
                sys.exit()

            # if btn[0] == "q":
                # print("q")
                # sys.exit()

def img_OCR(image,arduino):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    GaussianBlur = cv2.GaussianBlur(gray, (5, 5), 0)
    # cv2.imshow("GaussianBlur",GaussianBlur)

    th = cv2.adaptiveThreshold(GaussianBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    # cv2.imshow("th",th)

    # kernel = np.ones((3, 3), np.uint8)
    # dilate1 = cv2.erode(th, kernel, iterations = 1)
    # cv2.imshow("dilate1",dilate1)

    config = ('-l kor --oem 1 --psm 3')
    text = pytesseract.image_to_string(th,config=config)

    print(text)
    
    text_list = text.split() # 공백 기준으로 단어 split

    # braille_th = threading.Thread(target=convert_T2B,name="convert_T2B",args=(text_list))
    # braille_th.daemon = True
    # braille_list = braille_th.start()
    # braille_th.join()

    braille_list = convert_T2B(text_list) # 나눈 단어 점자 데이터로 변환
    print("데이터 변환 중...")
    print("변환 완료")
    print("전송 시작")  

    send_th = threading.Thread(target=send_T2B,name="send_T2B",args=(braille_list,arduino))
    send_th.daemon = True
    send_th.start()
    send_th.join()

    # send_T2B(braille_list,arduino) # 점자 데이터 전송  
    btn_detect_th = threading.Thread(target = btn_detect_I2T, name="btn_detect",args=(arduino,))
    btn_detect_th.daemon = True
    btn_detect_th.start()
    # cv2.waitKey(0)   

def mouse_handler(event, x, y, flags, param):
    global src 
    if event == cv2.EVENT_LBUTTONUP:
        if(len(src) == 4):
            pass
        else:
            src.append([x, y]) 
    if event == cv2.EVENT_RBUTTONUP:
        src = []
        cv2.destroyWindow("result")

def video_cap_I2T(arduino): 
    global src

    cv2.namedWindow('video')

    cap = cv2.VideoCapture(cv2.CAP_DSHOW)  

    codec = cv2.VideoWriter_fourcc(	'M', 'J', 'P', 'G'	)
    cap.set(6, codec)
    cap.set(5, 15)
    cap.set(3, 1920)
    cap.set(4, 1080)

    while 1:    
        ret, video = cap.read()  
        cv2.setMouseCallback('video', mouse_handler,video)

        height, width, channel = video.shape
        matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
        video = cv2.warpAffine(video, matrix, (width, height))
        
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
                img_OCR_th = threading.Thread(target = img_OCR, name="img_OCR",args = (result,arduino))
                img_OCR_th.daemon = True
                img_OCR_th.start()     
    sys.exit()