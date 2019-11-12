import time
import hgtk
from H2bMatch import *
import keyboard
import time
import serial


C_BOLD  = "\033[1m"
C_RED   = "\033[31m"
C_END   = "\033[0m"

def send(data_list):
    for data in data_list:
        print(data["letter"]+'['+C_BOLD+C_RED+data["braille"]+C_END+']', end=" ")  
    print("\n------------------------------------------------")
    binary_str = ""
    for data in data_list:
        binary_str += data["data"]
    # print(binary_str)
    arduino.write(binary_str.encode())
    wait = "0"
    print("아두이노 입력 대기 중...")
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
    braille_list = []

    print("점자데이터로 변환 중")
    for voca in text_list:
        # 약어 단어 O => 그러나 그래서 ... ...
        if abbr_H2b(voca):  
            temp = abbr_H2b(voca)
            temp['letter'] = voca
            braille_list.append(temp)
            braille_list.append(space_braille)
        # 약어 단어 X 
        else:   
            for letter in voca:
                # 약어 글자 O => 가 나 다    ...
                if abbr_H2b(letter):  
                    temp = abbr_H2b(letter)
                    temp['letter'] = letter
                    braille_list.append(temp)
                # 약어 글자 X
                else:  
                    # 한글 O
                    if hgtk.checker.is_hangul(letter):  
                        # 종성 O
                        if hgtk.checker.has_batchim(letter):  
                            element = hgtk.letter.decompose(letter)
                            temp = cho_H2b(element[0])
                            temp['letter'] = element[0]
                            braille_list.append(temp)

                            temp = joong_H2b(element[1])
                            temp['letter'] = element[1]
                            braille_list.append(temp)

                            temp = jong_H2b(element[2])
                            temp['letter'] = element[2]
                            braille_list.append(temp)
                        # 종성 X
                        else:  
                            element = hgtk.letter.decompose(letter)
                            temp = cho_H2b(element[0])
                            temp['letter'] = element[0]
                            braille_list.append(temp)

                            temp = joong_H2b(element[1])
                            temp['letter'] = element[1]
                            braille_list.append(temp)
                    # 한글 X
                    else:  
                        temp = no_han_H2b(letter)
                        temp['letter'] = letter
                        braille_list.append(temp)
            braille_list.append(space_braille)

    print("변환 완료")
    print("전송 시작")
    send_list = []
    for index, braille in enumerate(braille_list):
        if braille_length + braille['length'] < max_braille_length:
            send_list.append(braille)
            braille_length += braille['length']

        elif braille_length + braille['length'] == max_braille_length:  # 글자 길이 동일
            send_list.append(braille)

            send(send_list) 
            braille_length = 0
            send_list = []

        elif braille_length + braille['length'] > max_braille_length:  # 글자 길이 초과
            for i in range(0, max_braille_length - braille_length):
                send_list.append(space_braille)

            send(send_list)
            send_list = [braille]
            braille_length = braille['length']

        if index == len(braille_list)-1:  # 마지막 글자
            for i in range(0, max_braille_length - braille_length):
                send_list.append(space_braille)

            send(send_list) 
            braille_length = 0
            send_list = []
    
    end_str="000000/000000/000000/000000/"
    print(end_str)
    arduino.write(end_str.encode())
    print("전송 완료")
