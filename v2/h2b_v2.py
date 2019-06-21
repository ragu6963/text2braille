import hgtk
from change_v2 import cho_change,joong_change,jong_change,no_han_change 
max_length = 3 # 점자 길이
class h2b():
    def __init__(self):
        self.text = ""
        self.braill = ""  
        self.result_list = []

    def reset(self,length):
        for j in range(0,max_length-length):
            self.braill += "000000/"
        self.result_list.append(self.braill) 

    def convert(self):
        length = 0
        for i in range(0,len(self.text)):    
            letter = self.text
            if letter[i] != " " and hgtk.checker.is_hangul(letter[i]):  # 한글일 때 
                voca = hgtk.letter.decompose(letter[i])
                if hgtk.checker.has_batchim(letter[i]): # 종성이 있을 때
                    cho = voca[0] # 초성 획득 
                    joong = voca[1] # 중성 획득
                    jong = voca[2] # 종성 획득 
                    # 이전 점자 길이 + 현재 점자 길이가 max_length 보다 작을 떄
                    if (length + cho_change(cho)[1] + joong_change(joong)[1] + jong_change(jong)[1]) <= max_length:
                        self.braill += cho_change(cho)[0] + '/' 
                        self.braill += joong_change(joong)[0] + '/'
                        self.braill += jong_change(jong)[0] +'/'
                        length = length + cho_change(cho)[1] + joong_change(joong)[1] + jong_change(jong)[1] 

                    # 이전 점자 길이 + 현재 점자 길이가 max_length 보다 클 때    
                    else:
                        self.reset(length)
                        i = i - 1
                        self.braill = cho_change(cho)[0] + '/' 
                        self.braill += joong_change(joong)[0] + '/'
                        self.braill += jong_change(jong)[0] +'/'
                        length = cho_change(cho)[1] + joong_change(joong)[1] + jong_change(jong)[1] 

                else: # 종성이 없을 때
                    cho = voca[0] # 초성 획득
                    joong = voca[1] # 중성 획득

                    if (length + cho_change(cho)[1] + joong_change(joong)[1])  <= max_length: 
                        self.braill += cho_change(cho)[0] + '/'
                        self.braill += joong_change(joong)[0] +'/'  
                        length = length + cho_change(cho)[1] + joong_change(joong)[1] 

                    else: 
                        self.reset(length)
                        i = i - 1  
                        self.braill = cho_change(cho)[0] + '/'
                        self.braill += joong_change(joong)[0] +'/'
                        length = cho_change(cho)[1] + joong_change(joong)[1] 

            elif letter[i] != " " and not(hgtk.checker.is_hangul(letter[i])):  # 한글아닐 떄
                if (length + no_han_change(letter[i])[1]) <= max_length:
                    self.braill += no_han_change(letter[i])[0] +'/'
                    length += no_han_change(letter[i])[1]
                else: 
                    self.reset(length,i)
                    self.braill = no_han_change(letter[i])[0] +'/'
                    length = no_han_change(letter[i])[1]

            elif letter[i] == " ": # 공백일 때
                if (length+1) <= max_length:
                    self.braill += "000000/" 
                    length += 1
                else: 
                    self.reset(length)
                    i = i -1 
                    self.braill = "000000/"
                    length = 1

        for j in range(0,max_length-length):
            self.braill += "000000/"
        self.result_list.append(self.braill)


