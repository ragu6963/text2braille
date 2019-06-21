import serial,time 
from h2b_v2 import h2b as h2b
arduino = serial.Serial("COM6",9600) 

print("초기화중...")
time.sleep(3)
test = h2b()
test.text = input("text를 입력해주세요 : ")
test.convert()  
for i in range(0,len(test.result_list)): 
    print(test.result_list[i])
    arduino.write(test.result_list[i].encode())
    wait="0"
    while 1:
        if arduino.readable():
            wait = arduino.readline() 
            wait = wait.decode() 
            if wait[0] == "q": 
                break
        # wait=input("입력 대기중:")
        # if wait =="1":
        #     break