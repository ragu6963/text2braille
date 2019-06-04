import hgtk
from change_v2 import cho_change,joong_change,jong_change,no_han_change 
# 점자 길이
max_length = 4

class h2b():
    def __init__(self):
        self.글 = ""
        self.결과 = ""
        self.리스트 = []

    def reset(self,now_length,i):
        for j in range(0,max_length-now_length):
            self.결과 = self.결과 + "000000/"
        self.리스트.append(self.결과)
        i=i-1
        self.결과 = ""

    def convert(self):
        length = 0
        for i in range(0,len(self.글)):    
            if self.글[i] != " " and hgtk.checker.is_hangul(self.글[i]):  # 한글일 때
                cho = hgtk.letter.decompose(self.글[i])[0] # 초성 획득
                joong = hgtk.letter.decompose(self.글[i])[1] # 중성 획득
                jong = hgtk.letter.decompose(self.글[i])[2] # 종성 획득
                if jong != '': # 종성이 있을 때
                    # 이전 점자 길이 + 현재 점자 길이가 max_length 보다 작을 떄
                    if (length + cho_change(cho)[1] + joong_change(joong)[1] + jong_change(jong)[1]) <= max_length:
                        self.결과 = self.결과  + cho_change(cho)[0] + '/' 
                        self.결과 = self.결과  + joong_change(joong)[0] + '/'
                        self.결과 = self.결과  + jong_change(jong)[0] +'/'
                        length = length + cho_change(cho)[1] + joong_change(joong)[1] + jong_change(jong)[1] 
                    # 이전 점자 길이 + 현재 점자 길이가 max_length 보다 클 때    
                    else:
                        self.reset(length,i)
                        self.결과 = self.결과  + cho_change(cho)[0] + '/' 
                        self.결과 = self.결과  + joong_change(joong)[0] + '/'
                        self.결과 = self.결과  + jong_change(jong)[0] +'/'
                        length = cho_change(cho)[1] + joong_change(joong)[1] + jong_change(jong)[1] 

                else: # 종성이 없을 때
                    if (length + cho_change(cho)[1] + joong_change(joong)[1])  <= max_length:
                        self.결과 = self.결과 + cho_change(cho)[0] + '/'
                        self.결과 = self.결과 + joong_change(joong)[0] +'/'
                        length = length + cho_change(cho)[1] + joong_change(joong)[1] 
                    else:
                        # 남은 공간 공백으로 처리
                        self.reset(length,i)

                        self.결과 = self.결과 + cho_change(cho)[0] + '/'
                        self.결과 = self.결과 + joong_change(joong)[0] +'/'
                        length = cho_change(cho)[1] + joong_change(joong)[1] 

            elif self.글[i] != " " and not(hgtk.checker.is_hangul(self.글[i])):  # 한글아닐 떄
                if (length + no_han_change(self.글[i])[1]) <= max_length:
                    self.결과 = self.결과 + no_han_change(self.글[i])[0]
                    length += no_han_change(self.글[i])[1]
                else:
                    # 남은 공간 공백으로 처리
                    self.reset(length,i)

                    self.결과 = self.결과 + no_han_change(self.글[i])[0]
                    length = cho_change(cho)[1] + joong_change(joong)[1] 

            else: # 공백일 때
                if (length+1) <= max_length:
                    self.결과 = self.결과 + "000000/" 
                    length += 1
                else: 
                    self.reset(length,i) 
                    self.결과 = self.결과 + "000000/"
                    length = cho_change(cho)[1] + joong_change(joong)[1]

        for j in range(0,max_length-length):
            self.결과 = self.결과 + "000000/" 

        self.리스트.append(self.결과)
        self.리스트.append("000000/000000/000000/000000E")

    def output(self):
        for i in range(len(self.리스트)): 
            print(self.리스트[i])
            while(1):
                wait = input("대기중")
                if wait == '':
                    break   

