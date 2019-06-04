def cho_change(letter):
        if letter == 'ㄱ': 
                return ["000100",1]
        elif letter == 'ㄴ':
                return ["100100",1]
        elif letter == 'ㄷ':
                return ["010100",1]
        elif letter == 'ㄹ':
                return ["000010",1]
        elif letter == 'ㅁ':
                return ["100010",1]
        elif letter == 'ㅂ':
                return ["100100" ,1]
        elif letter == 'ㅅ':
                return ["000001" ,1]
        elif letter == 'ㅇ':
                return ["110110" ,1]
        elif letter == 'ㅈ':
                return ["000101" ,1]
        elif letter == 'ㅊ':
                return ["000011" ,1]
        elif letter == 'ㅋ':
                return ["110100" ,1]
        elif letter == 'ㅌ':
                return ["110010" ,1]
        elif letter == 'ㅍ': 
                return ["100110" ,1]
        elif letter == 'ㅎ':
                return ["010110" ,1]
        elif letter == 'ㄲ':
                return ["000001/000100" ,2]
        elif letter == 'ㄸ':
                return ["000001/010100" ,2]
        elif letter == 'ㅃ':
                return ["000001/000110" ,2]
        elif letter == 'ㅆ':
                return ["000001/000001" ,2]
        elif letter == 'ㅉ':
                return ["000001/000101" ,2] 
        else:
                return ["000000" ,1] 

def joong_change(letter): 
        if letter == 'ㅏ':
                return ["110001",1]
        elif letter == 'ㅑ':
                return ["001110",1]
        elif letter == 'ㅓ':
                return ["011100",1]
        elif letter == 'ㅕ':
                return ["100011",1]
        elif letter == 'ㅗ':
                return ["101001",1]
        elif letter == 'ㅛ': 
                return ["001101",1]
        elif letter == 'ㅜ':
                return ["101100",1]
        elif letter == 'ㅠ':
                return ["100101",1]
        elif letter == 'ㅡ':
                return ["010101",1]
        elif letter == 'ㅣ':
                return ["101010",1]
        elif letter == 'ㅐ':
                return ["111010",1]
        elif letter == 'ㅔ':
                return ["101110",1]
        elif letter == 'ㅒ':
                return ["001110/111010",2]
        elif letter == 'ㅖ':
                return ["001100",1]
        elif letter == 'ㅘ':
                return  ["111001",1]
        elif letter == 'ㅙ':
                return ["111001/111010",2]
        elif letter == 'ㅚ':
                return ["101111",1]
        elif letter == 'ㅝ':
                return ["111100",1]
        elif letter == 'ㅞ': 
                return ["111100/111010",2]
        elif letter == 'ㅟ':
                return ["101100/111010",2]
        elif letter == 'ㅢ': 
                return ["010111",1]
        else:
                return ["000000",1]
def jong_change(letter):
        if letter == 'ㄱ': 
                return  ["100000",1]
        elif letter == 'ㄴ':
                return ["010010",1]
        elif letter == 'ㄷ':
                return ["001010",1]
        elif letter == 'ㄹ':
                return ["010000",1]
        elif letter == 'ㅁ':
                return ["010001",1]
        elif letter == 'ㅂ':
                return ["110000",1]
        elif letter == 'ㅅ':
                return ["001000",1]
        elif letter == 'ㅇ':
                return ["011011",1]
        elif letter == 'ㅈ':
                return ["101000",1]
        elif letter == 'ㅊ':
                return ["011000",1]
        elif letter == 'ㅋ':
                return ["011010",1]
        elif letter == 'ㅌ':
                return ["011001",1]
        elif letter == 'ㅍ': 
                return ["010011",1]
        elif letter == 'ㅎ':
                return ["001011",1]
        elif letter == 'ㄲ':
                return ["100000/100000",2]
        elif letter == 'ㄳ':
                return ["100000/001000",2]
        elif letter == 'ㄵ':
                return ["010010/101000",2]
        elif letter == 'ㄶ':
                return ["010010/001011",2]
        elif letter == 'ㄺ':
                return ["010000/100000",2]
        elif letter == 'ㄻ':
                return  ["010000/010001",2]
        elif letter == 'ㄼ':
                return ["010000/110000",2]
        elif letter == 'ㄽ':
                return ["010000/001000",2]
        elif letter == 'ㄾ':
                return ["010000/011001",2]
        elif letter == 'ㄿ':
                return ["010000/010011",2]
        elif letter == 'ㅀ':
                return ["010000/001011",2]
        elif letter == 'ㅄ':
                return ["110000/001000",2]
        elif letter == 'ㅆ':
                return ["001100",1]

def no_han_change(letter):
        if letter == '1':
                return ["001111/100000",2]
        elif letter == '2':
                return ["001111/110000",2]
        elif letter == '3':
                return ["001111/100100",2]
        elif letter == '4':
                return ["001111/100110",2]
        elif letter == '5':
                return ["001111/100010",2]
        elif letter == '6':
                return ["001111/110100",2]
        elif letter == '7':
                return ["001111/110110",2]
        elif letter == '8':
                return ["001111/110010",2]
        elif letter == '9':
                return ["001111/010100",2]
        elif letter == '0':
                return ["001111/010110",2]
        elif letter == ',':
                return ["010000",1]
        elif letter == '.':
                return ["010011",1]
        elif letter == '-':
                return ["010010",1]
        elif letter == '?':
                return ["011001",1]
        elif letter == '_':
                return ["001001",1]
        elif letter == '!':
                return ["011010",1]
        else:
                return ["000000",1]
        

