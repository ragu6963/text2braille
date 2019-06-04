import serial,time 
from h2b import h2b
arduino = serial.Serial("COM7",9600) 

print("초기화중...")
time.sleep(2.5)
test = h2b()
test.글 = input("글을 입력해주세요 : ")
test.convert() 
wait = "0"
for i in range(len(test.리스트)): 
    print(test.리스트[i])
    arduino.write(test.리스트[i].encode())
    wait="0"
    while 1: 
        if arduino.readable():
            wait = arduino.readline() 
            wait = wait.decode() 
            print(wait)
            wait = str(wait) 
            if wait[0] == "1": 
                break   