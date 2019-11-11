braille = ["⠁","⠂","⠃","⠄","⠅",
"⠆","⠇","⠈","⠉","⠊","⠋","⠌","⠍",
"⠎","⠏","⠐","⠑","⠒","⠓","⠔","⠕",
"⠖","⠗","⠘","⠙","⠚","⠛","⠜","⠝",
"⠞","⠟",
"⠠","⠡","⠢","⠣","⠤","⠥","⠦","⠧",
"⠨","⠩","⠪","⠫","⠬","⠭","⠮","⠯",
"⠰","⠱","⠲","⠳","⠴","⠵","⠶","⠷",
"⠸","⠹","⠺","⠻","⠼","⠽","⠾","⠿",]
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
    if letter == '1':
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
