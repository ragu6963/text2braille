import serial
import time
from H2b import H2b
from H2bMatch import *

braille_length = 0
max_braille_length = 4
text = input("입력해주세요 : ")
# text = text.replace(" ", " ;")
text_list = text.split()  # 단어 기준으로 split
h2b_data = []
h2b_list = ""

for voca in text_list:
    if abbr_H2b(voca):  # 약어 단어 O => 그러나 그래서 ... ...

        # 점자길이 미초과시
        if (braille_length + abbr_H2b(voca)['length']) <= max_braille_length:
            braille_length += abbr_H2b(voca)['length'] + 1  # 점자 길이 추가
            h2b_data.append(abbr_H2b(voca)['data'])  # 송신 data 추가
            h2b_list += (abbr_H2b(voca)['braille'] + " ")  # 출력 점자문자 추가

        # 점자길이 초과시
        elif (braille_length + abbr_H2b(voca)['length']) > max_braille_length:
            for i in range(0, max_braille_length-braille_length+1):
                data = h2b_data.pop()
                h2b_data.append(data+"/000000")

            braille_length += abbr_H2b(voca)['length'] + 1  # 점자 길이 추가
            h2b_data.append(abbr_H2b(voca)['data'])  # 송신 data 추가
            h2b_list += (abbr_H2b(voca)['braille'] + " ")  # 출력 점자문자 추가

    else:   # 약어 단어 X
        if abbr_H2b(voca):  # 약어 글자 O => 가 나 다    ...
            pass
        else:  # 약어 글자 X
            pass
