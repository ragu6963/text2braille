import hgtk
import keyboard
import time
braille = ["⠁","⠂","⠃","⠄","⠅",
"⠆","⠇","⠈","⠉","⠊","⠋","⠌","⠍",
"⠎","⠏","⠐","⠑","⠒","⠓","⠔","⠕",
"⠖","⠗","⠘","⠙","⠚","⠛","⠜","⠝",
"⠞","⠟",
"⠠","⠡","⠢","⠣","⠤","⠥","⠦","⠧",
"⠨","⠩","⠪","⠫","⠬","⠭","⠮","⠯",
"⠰","⠱","⠲","⠳","⠴","⠵","⠶","⠷",
"⠸","⠹","⠺","⠻","⠼","⠽","⠾","⠿",]
space_braille = {"data": "000000/",
                "length": 1,
                "braille": " ",
                "letter": " "}


C_BOLD  = "\033[1m"
C_RED   = "\033[31m"
C_END   = "\033[0m"

def convert_H2b(text_list):
    braille_list = []
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
    return braille_list


def send_H2b(data_list):
    for data in data_list:
        print(data["letter"]+'['+C_BOLD+C_RED+data["braille"]+C_END+']', end=" ")  
    print("\n------------------------------------------------")
    binary_str = ""
    for data in data_list:
        binary_str += data["data"]
    print("아두이노 입력 대기 중...")
    
    # print(binary_str)
    # arduino.write(binary_str.encode())
    # wait = "0"
    
    # while 1:
    #     if arduino.readable():
    #         wait = arduino.readline()
    #         wait = wait.decode()
    #         if wait[0] == "q":
    #             break
    while 1:
        if keyboard.is_pressed('q'):
            time.sleep(0.1)
            break


def cho_H2b(letter):
    if letter == 'ㄱ':
        return {"data": "000100/",
                "length": 1,
                "braille": "⠈"}
    elif letter == 'ㄴ':
        return {"data": "100100/",
                "length": 1,
                "braille": "⠉"}
    elif letter == 'ㄷ':
        return {"data": "010100/",
                "length": 1,
                "braille": "⠊"}
    elif letter == 'ㄹ':
        return {"data": "000010/",
                "length": 1,
                "braille": "⠐"}
    elif letter == 'ㅁ':
        return {"data": "100010/",
                "length": 1,
                "braille": "⠑"}
    elif letter == 'ㅂ':
        return {"data": "000110/",
                "length": 1,
                "braille": "⠘"}
    elif letter == 'ㅅ':
        return {"data": "000001/",
                "length": 1,
                "braille": "⠠"}
    elif letter == 'ㅇ':
        return {"data": "011011/",
                "length": 1,
                "braille": "⠶"}
    elif letter == 'ㅈ':
        return {"data": "000101/",
                "length": 1,
                "braille": "⠨"}
    elif letter == 'ㅊ':
        return {"data": "000011/",
                "length": 1,
                "braille": "⠰"}
    elif letter == 'ㅋ':
        return {"data": "110100/",
                "length": 1,
                "braille": "⠋"}
    elif letter == 'ㅌ':
        return {"data": "110010/",
                "length": 1,
                "braille": "⠓"}
    elif letter == 'ㅍ':
        return {"data": "100110/",
                "length": 1,
                "braille": "⠙"}
    elif letter == 'ㅎ':
        return {"data": "010110/",
                "length": 1,
                "braille": "⠚"}
    elif letter == 'ㄲ':
        return {"data": "000001/000100/",
                "length": 2,
                "braille": "⠠⠈"}
    elif letter == 'ㄸ':
        return {"data": "000001/010100/",
                "length": 2,
                "braille": "⠠⠊"}
    elif letter == 'ㅃ':
        return {"data": "000001/000110/",
                "length": 2,
                "braille": "⠠⠘"}
    elif letter == 'ㅆ':
        return {"data": "000001/000001/",
                "length": 2,
                "braille": "⠠⠠"}
    elif letter == 'ㅉ':
        return {"data": "000001/000101/",
                "length": 2,
                "braille": "⠠⠨"}
    else:
        return {"data": "000000/",
                "length": 1,
                "braille": " "}


def joong_H2b(letter):
    if letter == 'ㅏ':
        return {"data": "110001/",
                "length": 1,
                "braille": "⠣"}
    elif letter == 'ㅑ':
        return {"data": "001110/",
                "length": 1,
                "braille": "⠜"}
    elif letter == 'ㅓ':
        return {"data": "011100/",
                "length": 1,
                "braille": "⠎"}
    elif letter == 'ㅕ':
        return {"data": "100011/",
                "length": 1,
                "braille": "⠱"}
    elif letter == 'ㅗ':
        return {"data": "101001/",
                "length": 1,
                "braille": "⠥"}
    elif letter == 'ㅛ':
        return {"data": "001101/",
                "length": 1,
                "braille": "⠬"}
    elif letter == 'ㅜ':
        return {"data": "101100/",
                "length": 1,
                "braille": "⠍"}
    elif letter == 'ㅠ':
        return {"data": "100101/",
                "length": 1,
                "braille": "⠩"}
    elif letter == 'ㅡ':
        return {"data": "010101/",
                "length": 1,
                "braille": "⠪"}
    elif letter == 'ㅣ':
        return {"data": "101010/",
                "length": 1,
                "braille": "⠕"}
    elif letter == 'ㅐ':
        return {"data": "111010/",
                "length": 1,
                "braille": "⠗"}
    elif letter == 'ㅔ':
        return {"data": "101110/",
                "length": 1,
                "braille": "⠝"}
    elif letter == 'ㅒ':
        return {"data": "001110/111010/",
                "length": 2,
                "braille": "⠜⠗"}
    elif letter == 'ㅖ':
        return {"data": "001100/",
                "length": 1,
                "braille": "⠌"}
    elif letter == 'ㅘ':
        return {"data": "111001/",
                "length": 1,
                "braille": "⠧"}
    elif letter == 'ㅙ':
        return {"data": "111001/111010/",
                "length": 2,
                "braille": "⠧⠗"}
    elif letter == 'ㅚ':
        return {"data": "101111/",
                "length": 1,
                "braille": "⠽"}
    elif letter == 'ㅝ':
        return {"data": "111100/",
                "length": 1,
                "braille": "⠏"}
    elif letter == 'ㅞ':
        return {"data": "111100/111010/",
                "length": 2,
                "braille": "⠏⠗"}
    elif letter == 'ㅟ':
        return {"data": "101100/111010/",
                "length": 2,
                "braille": "⠍⠗"}
    elif letter == 'ㅢ':
        return {"data": "010111/",
                "length": 1,
                "braille": "⠺"}
    else:
        return {"data": "000000/",
                "length": 1,
                "braille": " "}


def jong_H2b(letter):
    if letter == 'ㄱ':
        return {"data": "100000/",
                "length": 1,
                "braille": "⠁"}
    elif letter == 'ㄴ':
        return {"data": "010010/",
                "length": 1,
                "braille": "⠒"}
    elif letter == 'ㄷ':
        return {"data": "001010/",
                "length": 1,
                "braille": "⠔"}
    elif letter == 'ㄹ':
        return {"data": "010000/",
                "length": 1,
                "braille": "⠂"}
    elif letter == 'ㅁ':
        return {"data": "010001/",
                "length": 1,
                "braille": "⠢"}
    elif letter == 'ㅂ':
        return {"data": "110000/",
                "length": 1,
                "braille": "⠃"}
    elif letter == 'ㅅ':
        return {"data": "001000/",
                "length": 1,
                "braille": "⠄"}
    elif letter == 'ㅇ':
        return {"data": "011011/",
                "length": 1,
                "braille": "⠶"}
    elif letter == 'ㅈ':
        return {"data": "101000/",
                "length": 1,
                "braille": "⠅"}
    elif letter == 'ㅊ':
        return {"data": "011000/",
                "length": 1,
                "braille": "⠆"}
    elif letter == 'ㅋ':
        return {"data": "011010/",
                "length": 1,
                "braille": "⠖"}
    elif letter == 'ㅌ':
        return {"data": "011001/",
                "length": 1,
                "braille": "⠦"}
    elif letter == 'ㅍ':
        return {"data": "010011/",
                "length": 1,
                "braille": "⠲"}
    elif letter == 'ㅎ':
        return {"data": "001011/",
                "length": 1,
                "braille": "⠴"}
    elif letter == 'ㄲ':
        return {"data": "000001/100000/",
                "length": 2,
                "braille": "⠠⠁"}
    elif letter == 'ㄳ':
        return {"data": "100000/001000/",
                "length": 2,
                "braille": "⠁⠄"}
    elif letter == 'ㄵ':
        return {"data": "010010/101000/",
                "length": 2,
                "braille": "⠒⠅"}
    elif letter == 'ㄶ':
        return {"data": "010010/001011/",
                "length": 2,
                "braille": "⠒⠴"}
    elif letter == 'ㄺ':
        return {"data": "010000/100000/",
                "length": 2,
                "braille": "⠂⠁"}
    elif letter == 'ㄻ':
        return {"data": "010000/010001/",
                "length": 2,
                "braille": "⠂⠢"}
    elif letter == 'ㄼ':
        return {"data": "010000/110000/",
                "length": 2,
                "braille": "⠂⠃"}
    elif letter == 'ㄽ':
        return {"data": "010000/001000/",
                "length": 2,
                "braille": "⠂⠄"}
    elif letter == 'ㄾ':
        return {"data": "010000/011001/",
                "length": 2,
                "braille": "⠂⠦"}
    elif letter == 'ㄿ':
        return {"data": "010000/010011/",
                "length": 2,
                "braille": "⠂⠲"}
    elif letter == 'ㅀ':
        return {"data": "010000/001011/",
                "length": 2,
                "braille": "⠂⠴"}
    elif letter == 'ㅄ':
        return {"data": "110000/001000/",
                "length": 2,
                "braille": "⠃⠄"}
    elif letter == 'ㅆ':
        return {"data": "001100/",
                "length": 1,
                "braille": "⠌"}


def no_han_H2b(letter):
    if letter == 'a' or letter == 'A':
        return {"data": "001011/100000/",
                "length": 2,
                "braille": "⠴⠁"}
    elif letter == 'b' or letter == 'B':
        return {"data": "001011/110000/",
                "length": 2,
                "braille": "⠴⠃"}
    elif letter == 'c' or letter == 'C':
        return {"data": "001011/100100/",
                "length": 2,
                "braille": "⠴⠉"}
    elif letter == 'd' or letter == 'D':
        return {"data": "001011/100110/",
                "length": 2,
                "braille": "⠴⠙"}
    elif letter == 'e' or letter == 'E':
        return {"data": "001011/100010/",
                "length": 2,
                "braille": "⠴⠑"}
    elif letter == 'f' or letter == 'F':
        return {"data": "001011/110100/",
                "length": 2,
                "braille": "⠴⠋"}
    elif letter == 'g' or letter == 'G':
        return {"data": "001011/110110/",
                "length": 2,
                "braille": "⠴⠛"}
    elif letter == 'h' or letter == 'H':
        return {"data": "001011/110010/",
                "length": 2,
                "braille": "⠴⠓"}
    elif letter == 'i' or letter == 'I':
        return {"data": "001011/010100/",
                "length": 2,
                "braille": "⠴⠊"}
    elif letter == 'j' or letter == 'J':
        return {"data": "001011/010110/",
                "length": 2,
                "braille": "⠴⠚"}
    elif letter == 'k' or letter == 'K':
        return {"data": "001011/101000/",
                "length": 2,
                "braille": "⠴⠅"}
    elif letter == 'l' or letter == 'L':
        return {"data": "001011/111000/",
                "length": 2,
                "braille": "⠴⠇"}
    elif letter == 'm' or letter == 'M':
        return {"data": "001011/101100/",
                "length": 2,
                "braille": "⠴⠍"}
    elif letter == 'n' or letter == 'N':
        return {"data": "001011/101110/",
                "length": 2,
                "braille": "⠴⠝"}
    elif letter == 'o' or letter == 'O':
        return {"data": "001011/101010/",
                "length": 2,
                "braille": "⠴⠕"}
    elif letter == 'p' or letter == 'P':
        return {"data": "001011/111100/",
                "length": 2,
                "braille": "⠴⠏"}
    elif letter == 'q' or letter == 'Q':
        return {"data": "001011/111110/",
                "length": 2,
                "braille": "⠴⠟"}
    elif letter == 'r' or letter == 'R':
        return {"data": "001011/111010/",
                "length": 2,
                "braille": "⠴⠗"}
    elif letter == 's' or letter == 'S':
        return {"data": "001011/011100/",
                "length": 2,
                "braille": "⠴⠎"}
    elif letter == 't' or letter == 'T':
        return {"data": "001011/011110/",
                "length": 2,
                "braille": "⠴⠞"}
    elif letter == 'u' or letter == 'U':
        return {"data": "001011/101001/",
                "length": 2,
                "braille": "⠴⠥"}
    elif letter == 'v' or letter == 'V':
        return {"data": "001011/111001/",
                "length": 2,
                "braille": "⠴⠧"}
    elif letter == 'w' or letter == 'W':
        return {"data": "001011/010111/",
                "length": 2,
                "braille": "⠴⠺"}
    elif letter == 'x' or letter == 'X':
        return {"data": "001011/101101/",
                "length": 2,
                "braille": "⠴⠭"}
    elif letter == 'y' or letter == 'Y':
        return {"data": "001011/101111/",
                "length": 2,
                "braille": "⠴⠽"}
    elif letter == 'z' or letter == 'Z':
        return {"data": "001011/101011/",
                "length": 2,
                "braille": "⠴⠵"}
    elif letter == '1':
        return {"data": "001111/100000/",
                "length": 2,
                "braille": "⠼⠁"}
    elif letter == '2':
        return {"data": "001111/110000/",
                "length": 2,
                "braille": "⠼⠃"}
    elif letter == '3':
        return {"data": "001111/100100/",
                "length": 2,
                "braille": "⠼⠉"}
    elif letter == '4':
        return {"data": "001111/100110/",
                "length": 2,
                "braille": "⠼⠙"}
    elif letter == '5':
        return {"data": "001111/100010/",
                "length": 2,
                "braille": "⠼⠑"}
    elif letter == '6':
        return {"data": "001111/110100/",
                "length": 2,
                "braille": "⠼⠋"}
    elif letter == '7':
        return {"data": "001111/110110/",
                "length": 2,
                "braille": "⠼⠛"}
    elif letter == '8':
        return {"data": "001111/110010/",
                "length": 2,
                "braille": "⠼⠓"}
    elif letter == '9':
        return {"data": "001111/010100/",
                "length": 2,
                "braille": "⠼⠊"}
    elif letter == '0':
        return {"data": "001111/010110/",
                "length": 2,
                "braille": "⠼⠚"}
    elif letter == ',':
        return {"data": "010000/",
                "length": 1,
                "braille": "⠂"}
    elif letter == '.':
        return {"data": "010011/",
                "length": 1,
                "braille": "⠄"}
    elif letter == '-':
        return {"data": "010010/",
                "length": 1,
                "braille": "⠤"}
    elif letter == '?':
        return {"data": "011001/",
                "length": 1,
                "braille": "⠦"}
    elif letter == '_':
        return {"data": "001001/",
                "length": 1,
                "braille": "⠤"}
    elif letter == '!':
        return {"data": "011010/",
                "length": 1,
                "braille": "⠖"}  
    elif letter == ':':
        return {"data": "000010/010000/",
                "length": 2,
                "braille": "⠐⠂"}
    elif letter == ';':
        return {"data": "000011/011000/",
                "length": 2,
                "braille": "⠰⠆"}
    
    else:
        return {"data": "000000/",
                "length": 1,
                "braille": " "}

def abbr_H2b(letter):
    if letter == "가":
        return {"data": "110101/",
                "length": 1,
                "braille": "⠫"}
    elif letter == "나":
        return {"data": "100100/",
                "length": 1,
                "braille": "⠉"}
    elif letter == "다":
        return {"data": "010100/",
                "length": 1,
                "braille": "⠊"}
    elif letter == "마":
        return {"data": "100010/",
                "length": 1,
                "braille": "⠑"}
    elif letter == "바":
        return {"data": "000110/",
                "length": 1,
                "braille": "⠘"}
    elif letter == "사":
        return {"data": "111000/",
                "length": 1,
                "braille": "⠇"}
    elif letter == "자":
        return {"data": "000101/",
                "length": 1,
                "braille": "⠨"}
    elif letter == "카":
        return {"data": "110100/",
                "length": 1,
                "braille": "⠋"}
    elif letter == "타":
        return {"data": "110010/",
                "length": 1,
                "braille": "⠓"}
    elif letter == "파":
        return {"data": "100110/",
                "length": 1,
                "braille": "⠙"}
    elif letter == "하":
        return {"data": "010110/",
                "length": 1,
                "braille": "⠚"}
    elif letter == "것":
        return {"data": "000111/011100/",
                "length": 2,
                "braille": "⠸⠎"}
    elif letter == "억":
        return {"data": "100111/",
                "length": 1,
                "braille": "⠹"}
    elif letter == "언":
        return {"data": "011111/",
                "length": 1,
                "braille": "⠾"}
    elif letter == "얼":
        return {"data": "011110/",
                "length": 1,
                "braille": "⠞"}
    elif letter == "연":
        return {"data": "100001/",
                "length": 1,
                "braille": "⠡"}
    elif letter == "열":
        return {"data": "110011/",
                "length": 1,
                "braille": "⠳"}
    elif letter == "영":
        return {"data": "110111/",
                "length": 1,
                "braille": "⠻"}
    elif letter == "옥":
        return {"data": "101101/",
                "length": 1,
                "braille": "⠭"}
    elif letter == "온":
        return {"data": "111011/",
                "length": 1,
                "braille": "⠷"}
    elif letter == "옹":
        return {"data": "111111/",
                "length": 1,
                "braille": "⠿"}
    elif letter == "운":
        return {"data": "110110/",
                "length": 1,
                "braille": "⠛"}
    elif letter == "울":
        return {"data": "111101/",
                "length": 1,
                "braille": "⠯"}
    elif letter == "은":
        return {"data": "101011/",
                "length": 1,
                "braille": "⠵"}
    elif letter == "을":
        return {"data": "011101/",
                "length": 1,
                "braille": "⠮"}
    elif letter == "인":
        return {"data": "111110/",
                "length": 1,
                "braille": "⠟"}
    elif letter == "그래서":
        return {"data": "100000/011100/",
                "length": 2,
                "braille": "⠁⠎"}
    elif letter == "그러면":
        return {"data": "100000/010010/",
                "length": 2,
                "braille": "⠁⠒"}
    elif letter == "그러나":
        return {"data": "100000/100100/",
                "length": 2,
                "braille": "⠁⠉"}
    elif letter == "그러므로":
        return {"data": "100000/010001/",
                "length": 2,
                "braille": "⠁⠢"}
    elif letter == "그런데":
        return {"data": "100000/101110/",
                "length": 2,
                "braille": "⠁⠝"}
    elif letter == "그리고":
        return {"data": "100000/101001/",
                "length": 2,
                "braille": "⠁⠥"}
    elif letter == "그리하여":
        return {"data": "100000/100011/",
                "length": 2,
                "braille": "⠁⠱"}
    elif letter == " ":
        return {"data": "000000/",
                "length": 1,
                "braille": " "}


