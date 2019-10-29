import time
import hgtk
from H2bMatch import *

space_braille = {"data": "000000",
                "length": 1,
                "braille": " ",
                "letter": " "} 

braille_length = 0
max_braille_length = 4

text = input("입력해주세요 : ")
text_list = text.split()  # 단어 기준으로 split
braille_list = []
h2b_list = ""

print("변환 중...")
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
                    if hgtk.checker.has_batchim(letter): # 종성 O
                        element = hgtk.letter.decompose(letter)
                        braille = cho_H2b(element[0])    
                        braille['letter'] = element[0]
                        braille_list.append(braille)

                        braille = joong_H2b(element[1])    
                        braille['letter'] = element[1]
                        braille_list.append(braille)

                        braille = jong_H2b(element[2])    
                        braille['letter'] = element[2]
                        braille_list.append(braille)
                    else: # 종성 X
                        element = hgtk.letter.decompose(letter)
                        braille = cho_H2b(element[0])    
                        braille['letter'] = element[0]
                        braille_list.append(braille)

                        braille = joong_H2b(element[1])    
                        braille['letter'] = element[1]
                        braille_list.append(braille)
                else: # 한글 X
                    braille = no_han_H2b(letter)
                    braille['letter'] = letter
                    braille_list.append(braille)

        braille_list.append(space_braille)

print("변환 완료")
for b in braille_list:

    print(b)
