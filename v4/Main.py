import serial
import time
import hgtk
from H2b import H2b
from H2bMatch import *

braille_length = 0
max_braille_length = 4
text = input("입력해주세요 : ")
text_list = text.split()  # 단어 기준으로 split
braille_list = []
h2b_list = ""

for voca in text_list:
    if abbr_H2b(voca):  # 약어 단어 O => 그러나 그래서 ... ...
        braille = abbr_H2b(voca)
        braille['letter'] = voca
        braille_list.append(braille)
    else:   # 약어 단어 X
        for letter in voca:
            if abbr_H2b(letter):  # 약어 글자 O => 가 나 다    ...
                braille = abbr_H2b(letter)
                braille['letter'] = letter
                braille_list.append(braille)
            else:  # 약어 글자 X
                if hgtk.checker.is_hangul(letter): # 한글 O
                    letter = hgtk.letter.decompose(letter)
                    
                    braille = cho_H2b(letter[0])
                    braille['letter'] = letter[0]
                    braille_list.append(braille)
                else: # 한글 X
                    pass

for b in braille_list:
    print(b)
