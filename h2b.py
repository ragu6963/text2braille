import hgtk
from change import cho_change,joong_change,jong_change,no_han_change


class h2b():
    def __init__(self):
        self.글 = ""
        self.결과 = ""
        self.리스트 = []

    def convert(self):
        for i in range(len(self.글)):
            if i % 2 != 0:
                self.결과 = self.결과 + '#'

            if self.글[i] != " " and hgtk.checker.is_hangul(self.글[i]):  # 한글일 때
                cho = hgtk.letter.decompose(self.글[i])[0]
                joong = hgtk.letter.decompose(self.글[i])[1]
                jong = hgtk.letter.decompose(self.글[i])[2]
                if jong != '':
                    self.결과 = self.결과  + cho_change(cho) + '/'
                    self.결과 = self.결과 + joong_change(joong) + '/'
                    self.결과 = self.결과  + jong_change(jong) 
                else:
                    self.결과 = self.결과 + cho_change(cho) + '/'
                    self.결과 = self.결과 + joong_change(joong) 

            elif self.글[i] != " " and not(hgtk.checker.is_hangul(self.글[i])):  # 한글아닐 떄
                self.결과 = self.결과 + no_han_change(self.글[i])

            else:  # 공백일 때
                self.결과 = self.결과 + "000000" 
 
            
            if i % 2 == 0: # 앞 글자에 
                self.결과 = 'Q' + self.결과 

            if i == len(self.글)-1: # 마지막 글자일경우 무조건 리스트에 APPEND
                self.결과 = self.결과 + 'E'
                self.리스트.append(self.결과)
                self.결과 = "" 

            elif i % 2 != 0: # 홀수 인덱스(1,3,5,7...) == 두번째 글자 마다 리스트에 APPEND   
                self.리스트.append(self.결과)
                self.결과 = "" 

    def output(self):
        for i in range(len(self.리스트)): 
            print(self.리스트[i])
            while(1):
                wait = input("대기중")
                if wait == '':
                    break   

