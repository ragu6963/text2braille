import time
import hgtk 
import keyboard
import time
import serial
from H2bMatch import *





arduino = serial.Serial("COM4", 9600)
print("초기화중...")
# time.sleep(3)

space_braille = {"data": "000000/",
                "length": 1,
                "braille": " ",
                "letter": " "}
braille_length = 0
max_braille_length = 4

while 1: 
    text = input("텍스트를 입력해주세요 : ")
    text_list = text.split()  # 단어 기준으로 split 
    print("점자데이터로 변환 중")
    print("변환 완료")
    braille_list = convert_H2b(text_list)
    print("전송 시작")
    send_list = []
    for index, braille in enumerate(braille_list):
        if braille_length + braille['length'] < max_braille_length:
            send_list.append(braille)
            braille_length += braille['length']

        elif braille_length + braille['length'] == max_braille_length:  # 글자 길이 동일
            send_list.append(braille)

            send_H2b(send_list) 
            braille_length = 0
            send_list = []

        elif braille_length + braille['length'] > max_braille_length:  # 글자 길이 초과
            for i in range(0, max_braille_length - braille_length):
                send_list.append(space_braille)

            send_H2b(send_list)
            send_list = [braille]
            braille_length = braille['length']

        if index == len(braille_list)-1:  # 마지막 글자
            for i in range(0, max_braille_length - braille_length):
                send_list.append(space_braille)

            send_H2b(send_list) 
            braille_length = 0
            send_list = []
    
    
    # end_str="000000/000000/000000/000000/"
    # print(end_str)
    # arduino.write(end_str.encode())
    print("전송 완료")
