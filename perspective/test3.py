import cv2
import numpy as np
import mapper
import sys
import pytesseract

cap = cv2.VideoCapture(0)
while(True):
    ret, img = cap.read()
    img = cv2.resize(img,(1300,800))
    cv2.imshow("img",img)
    copy = img.copy()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred =cv2.GaussianBlur(gray,(5,5),0)
    edge = cv2.Canny(blurred,30,50)

    contours,__ = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    
    for c in contours:
        p = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*p,True)

        if len(approx) == 4:
            target = approx
            break

    approx = mapper.mapp(target)
    pts = np.float32([[0,0],[800,0],[800,800],[0,800]])
    op = cv2.getPerspectiveTransform(approx,pts)
    dst = cv2.warpPerspective(copy,op,(800,800))

    cv2.imshow("dst",dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# dst = cv2.imread("./test1.png")
# dst = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
# blurred =cv2.GaussianBlur(gray,(5,5),0)
# edge = cv2.Canny(blurred,30,50)
# cv2.imshow("edge",edge)
# cv2.waitKey(0)

config = ('--tessdata-dir "tessdata" -l eng --oem 1 --psm 3')
config = ('-l kor ')

text = pytesseract.image_to_string(dst,lang="Hangul")
print(text)
