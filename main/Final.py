# -*- coding: utf-8 -*- 
def nothing(x):
    pass
import time
import hgtk 
import keyboard
import time
import serial
import cv2
import numpy as np
import pytesseract
import sys
from H2bMatch import *

arduino = serial.Serial("/dev/ttyACM2", 9600)
print("초기화 중")
# time.sleep(3)

space_braille = {"data": "000000/",
                "length": 1,
                "braille": " ",
                "letter": " "}
now_braille_length = 0
max_braille_length = 4

while(True):
    print("원하는 방식을 입력해 주세요.")
    print("1.텍스트 직접 입력 , 2.이미지 촬영(OCR) , 3.프로그램 종료")
    mod = input()
    if(mod == "1"):
        text = input("텍스트를 입력해주세요 : ")
        text_list = text.split()  # 단어 기준으로 split 
        print("점자데이터로 변환 중")
        braille_list = convert_H2b(text_list)
        print("변환 완료")
        print("전송 시작")

        send_list = []

        for index, send_data in enumerate(braille_list):
            length = send_data['length'] 

            if now_braille_length + length < max_braille_length:
                send_list.append(send_data)
                now_braille_length += length

            elif now_braille_length + length == max_braille_length:  # 글자 길이 동일
                send_list.append(send_data)

                send_H2b(send_list,arduino) 
                now_braille_length = 0
                send_list = []

            elif now_braille_length + length > max_braille_length:  # 글자 길이 초과
                for i in range(0, max_braille_length - now_braille_length):
                    send_list.append(space_braille)

                send_H2b(send_list,arduino)
                send_list = [send_data]
                now_braille_length = length

            if index == len(braille_list)-1:  # 마지막 글자
                for i in range(0, max_braille_length - now_braille_length):
                    send_list.append(space_braille)

                send_H2b(send_list,arduino) 
                now_braille_length = 0
                send_list = [] 
        print("전송 완료")
    elif(mod == "2"): 
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

                    # wait = arduino.readline()
                    # wait = wait.decode()
                    # if wait[0] == "p":
                # if arduino.readable():
                #     wait = arduino.readline()
                #     wait = wait.decode()
                #     if wait[0] == "p":
                #         break
                    

            cap.release()
            cv2.destroyAllWindows() 
            print("입력 대기 중")
            while 1:
                if arduino.readable():
                    wait = arduino.readline()
                    wait = wait.decode()
                    if wait[0] == "q":
                        break
            # while 1:    
            #     if keyboard.is_pressed('q'):
            #         time.sleep(0.1)
            #         break 
    elif(mod =="3"):
        sys.exit()