import time 
import serial  
from Text2Braille import *
# import Text2Braille as tb 

arduino = serial.Serial("COM4", 9600)
print("초기화 중")
time.sleep(1.5)  

while(True): 
    text = input("텍스트를 입력해주세요 : ")
    text_list = text.split() # 공백 기준으로 단어 split
    print("데이터 변환 시작")
    braille_list = convert_T2B(text_list) # 나눈 단어 점자 데이터로 변환
    print("데이터 변환 완료")
    print("전송 시작")   
    send_T2B(braille_list,arduino) # 점자 데이터 전송  
