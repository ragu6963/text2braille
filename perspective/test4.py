import cv2
import numpy as np
import mapper
import sys
import pytesseract

cap = cv2.VideoCapture(0)
while(True):
    ret, img = cap.read() 
    cv2.circle(img, (100, 50), 5, (0, 0, 255), -1)
    cv2.circle(img, (600, 50), 5, (0, 0, 255), -1)
    cv2.circle(img, (100, 400), 5, (0, 0, 255), -1)
    cv2.circle(img, (600, 400), 5, (0, 0, 255), -1)

    pts1 = np.float32([[100, 50], [600, 50], [100, 400], [600, 400]])
    height, weight = img.shape[:2]
    pts2 = np.float32([[0, 0], [weight, 0], [0, height], [weight, height]])
    mat = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, mat, (weight, height))
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    cv2.imshow("gray",gray)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# cv2.imshow("img",img)
# img = cv2.imread("./test1.png")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# blurred =cv2.GaussianBlur(gray,(5,5),0)
# edge = cv2.Canny(blurred,30,50)
# cv2.imshow("edge",edge)
# cv2.imshow("img",img)
cv2.waitKey(0)
# config = ('--tessdata-dir "tessdata" -l kor --oem 1 --psm 3')
# config = ('-l kor ')
text = pytesseract.image_to_string(gray,config='--psm 1 --oem 3')
print(text)