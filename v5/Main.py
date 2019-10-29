import time
import hgtk
from H2bMatch import *


space_braille = {"data": "000000/",
                "length": 1,
                "braille": " ",
                "letter": " "}

braille_length = 0
max_braille_length = 4

while 1:
    text = input("입력해주세요 : ")
    text_list = text.split()  # 단어 기준으로 split
    braille_list = []

    print("변환 중...")
    for voca in text_list:
        if abbr_H2b(voca):  # 약어 단어 O => 그러나 그래서 ... ...
            temp = abbr_H2b(voca)
            temp['letter'] = voca
            braille_list.append(temp)
            braille_list.append(space_braille)

        else:   # 약어 단어 X
            for letter in voca:
                if abbr_H2b(letter):  # 약어 글자 O => 가 나 다    ...
                    temp = abbr_H2b(letter)
                    temp['letter'] = letter
                    braille_list.append(temp)
                else:  # 약어 글자 X
                    if hgtk.checker.is_hangul(letter):  # 한글 O
                        if hgtk.checker.has_batchim(letter):  # 종성 O
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
                        else:  # 종성 X
                            element = hgtk.letter.decompose(letter)
                            temp = cho_H2b(element[0])
                            temp['letter'] = element[0]
                            braille_list.append(temp)

                            temp = joong_H2b(element[1])
                            temp['letter'] = element[1]
                            braille_list.append(temp)
                    else:  # 한글 X
                        temp = no_han_H2b(letter)
                        temp['letter'] = letter
                        braille_list.append(temp)
            braille_list.append(space_braille)

    print("변환 완료")
    send_list = []

    for index, braille in enumerate(braille_list):
        if braille_length + braille['length'] < max_braille_length:
            send_list.append(braille)
            braille_length += braille['length']

        elif braille_length + braille['length'] == max_braille_length:  # 글자 길이 초과
            send_list.append(braille)

            for send_data in send_list:
                print(send_data["letter"], end="")  # 송신
            for send_data in send_list:
                print(send_data["data"], end="")  # 송신
            print("\n------------")

            braille_length = 0
            send_list = []

        elif braille_length + braille['length'] > max_braille_length:  # 글자 길이 초과
            for i in range(0, max_braille_length - braille_length):
                send_list.append(space_braille)

            for send_data in send_list:
                print(send_data["letter"], end="")  # 송신
            for send_data in send_list:
                print(send_data["data"], end="")  # 송신
            print("\n------------")

            send_list = [braille]
            braille_length = braille['length']

        if index == len(braille_list)-1:  # 마지막 글자
            for i in range(0, max_braille_length - braille_length):
                send_list.append(space_braille)

            for send_data in send_list:
                print(send_data["letter"], end="")  # 송신
            for send_data in send_list:
                print(send_data["data"], end="")  # 송신

            print("\n------------")
            braille_length = 0
            send_list = []
