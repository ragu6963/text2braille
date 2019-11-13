import pytesseract
import cv2 

# try:
#     import Image
# except ImportError:
#     from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# print(pytesseract.image_to_string(Image.open('messigray.png'), lang='Kor'))


# print(pytesseract.image_to_string('messigray.png'))
# 카메라에 접근하기 위해 VideoCapture 객체를 생성
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
while(True):
    ret, img_color = cap.read()

    if ret == False:
        break

    cv2.imshow('img_color', img_color)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) 

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()