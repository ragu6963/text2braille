import time 
import serial  
import threading
import pyautogui   
from Image2Text import *  

arduino = serial.Serial("COM4", 9600)
print("초기화 중") 
time.sleep(1.5)  
print("시작")  

btn_detect_th = threading.Thread(target = btn_detect_I2T, name="btn_detect_I2T",args=(arduino,))
btn_detect_th.daemon = True
btn_detect_th.start() 

video_cap_th = threading.Thread(target = video_cap_I2T, name="video",args=(arduino,))
video_cap_th.start() 