import serial,time 
from h2b_v2 import h2b as h2b
# arduino = serial.Serial("COM6",9600) 

# print("초기화중...")
# time.sleep(3)
test = h2b()
test.글 = input("글을 입력해주세요 : ")
test.convert()
# arduino.write(test.리스트[0].encode())
# test.output() 
wait = "0"
for i in range(0,len(test.리스트)): 
    print(test.리스트[i])
    # arduino.write(test.리스트[i].encode())
    wait="0"
    while 1: 
        # if arduino.readable():
        #     wait = arduino.readline() 
        #     wait = wait.decode() 
        #     print(wait) 
        #     if wait[0] == "1": 
        #         break   
        wait=input("입력 대기중:")
        if wait =="1":
            break