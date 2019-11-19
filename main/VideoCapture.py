import time 
import serial  
from Image2Text import * 

arduino = serial.Serial("COM5", 9600)
print("초기화 중")
# time.sleep(3) 

btn_detect_th = threading.Thread(target = btn_detect_I2T, name="btn_detect",args=(arduino,))
btn_detect_th.start()

video_cap_th = threading.Thread(target = video_cap_I2T, name="video")
video_cap_th.start() 

