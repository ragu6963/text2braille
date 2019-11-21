import time 
import serial  
from Image2Text import * 

arduino = serial.Serial("COM5", 9600)
print("초기화 중")
# time.sleep(3)  


video_cap_th = threading.Thread(target = video_cap_I2T, name="video",args=(arduino,))
video_cap_th.start() 