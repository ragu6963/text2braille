def cho_change(letter):
        if letter == 'ㄱ': 
                return "000100"
        elif letter == 'ㄴ':
                return "100100"
        elif letter == 'ㄷ':
                return "010100"
        elif letter == 'ㄹ':
                return "000010"
        elif letter == 'ㅁ':
                return "100010"
        elif letter == 'ㅂ':
                return "100100"
        elif letter == 'ㅅ':
                return "000001"
        elif letter == 'ㅇ':
                return "110110"
        elif letter == 'ㅈ':
                return "000101"
        elif letter == 'ㅊ':
                return "000011"
        elif letter == 'ㅋ':
                return "110100"
        elif letter == 'ㅌ':
                return "110010"
        elif letter == 'ㅍ': 
                return "100110"
        elif letter == 'ㅎ':
                return "010110"
        elif letter == 'ㄲ':
                return "000001/000100"
        elif letter == 'ㄸ':
                return "000001/010100"
        elif letter == 'ㅃ':
                return "000001/000110"
        elif letter == 'ㅆ':
                return "000001/000001"
        elif letter == 'ㅉ':
                return "000001/000101" 
        
        else:
                return "000000"
def joong_change(letter): 
        if letter == 'ㅏ':
                return "110001"
        elif letter == 'ㅑ':
                return "001110"
        elif letter == 'ㅓ':
                return "011100"
        elif letter == 'ㅕ':
                return "100011"
        elif letter == 'ㅗ':
                return "101001"
        elif letter == 'ㅛ': 
                return "001101"
        elif letter == 'ㅜ':
                return "101100"
        elif letter == 'ㅠ':
                return "100101"
        elif letter == 'ㅡ':
                return "010101"
        elif letter == 'ㅣ':
                return "101010"
        elif letter == 'ㅐ':
                return "111010"
        elif letter == 'ㅔ':
                return "101110"
        elif letter == 'ㅒ':
                return "001110/111010"
        elif letter == 'ㅖ':
                return "001100"
        elif letter == 'ㅘ':
                return "111001"
        elif letter == 'ㅙ':
                return "111001/111010"
        elif letter == 'ㅚ':
                return "101111"
        elif letter == 'ㅝ':
                return "111100"
        elif letter == 'ㅞ': 
                return "111100/111010"
        elif letter == 'ㅟ':
                return "101100/111010"
        elif letter == 'ㅢ': 
                return "010111"
        else:
                return "000000" 
def jong_change(letter):
        if letter == 'ㄱ': 
                return "100000"
        elif letter == 'ㄴ':
                return "010010"
        elif letter == 'ㄷ':
                return "001010"
        elif letter == 'ㄹ':
                return "010000"
        elif letter == 'ㅁ':
                return "010001"
        elif letter == 'ㅂ':
                return "110000"
        elif letter == 'ㅅ':
                return "001000"
        elif letter == 'ㅇ':
                return "011011"
        elif letter == 'ㅈ':
                return "101000"
        elif letter == 'ㅊ':
                return "011000"
        elif letter == 'ㅋ':
                return "011010"
        elif letter == 'ㅌ':
                return "011001"
        elif letter == 'ㅍ': 
                return "010011"
        elif letter == 'ㅎ':
                return "001011"
        elif letter == 'ㄲ':
                return "100000/100000"
        elif letter == 'ㄳ':
                return "100000/001000"
        elif letter == 'ㄵ':
                return "010010/101000"
        elif letter == 'ㄶ':
                return "010010/001011"
        elif letter == 'ㄺ':
                return "010000/100000"
        elif letter == 'ㄻ':
                return "010000/010001" 
        elif letter == 'ㄼ':
                return "010000/110000"
        elif letter == 'ㄽ':
                return "010000/001000"
        elif letter == 'ㄾ':
                return "010000/011001"
        elif letter == 'ㄿ':
                return "010000/010011"
        elif letter == 'ㅀ':
                return "010000/001011"
        elif letter == 'ㅄ':
                return "110000/001000"
        elif letter == 'ㅆ':
                return "001100";

def no_han_change(letter):
        if letter == '1':
                return "001111/100000"
        elif letter == '2':
                return "001111/110000"
        elif letter == '3':
                return "001111/100100"
        elif letter == '4':
                return "001111/100110"
        elif letter == '5':
                return "001111/100010"
        elif letter == '6':
                return "001111/110100"
        elif letter == '7':
                return "001111/110110"
        elif letter == '8':
                return "001111/110010"
        elif letter == '9':
                return "001111/010100"
        elif letter == '0':
                return "001111/010110"
        elif letter == ',':
                return "010000"
        elif letter == '.':
                return "010011"
        elif letter == '-':
                return "010010"
        elif letter == '?':
                return "011001"
        elif letter == '_':
                return "001001"
        elif letter == '!':
                return "011010" 
        else:
                return "000000"
        

