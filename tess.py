import pytesseract
import cv2 as cv

try:
    import Image
except ImportError:
    from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(Image.open('messigray.png'), lang='Kor'))


# print(pytesseract.image_to_string('messigray.png'))
# # 카메라에 접근하기 위해 VideoCapture 객체를 생성
# cap = cv.VideoCapture(0)

# while(True):
#     ret, img_color = cap.read()
#     if ret == False:
#         break;

#     img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
#     cv.imshow('gray', img_gray)

#     # ESC 키누르면 종료
#     if cv.waitKey(1) & 0xFF == 27:
#         cv.imwrite('messigray.png',img_gray, params=[cv.IMWRITE_PNG_COMPRESSION,0])
#         break


# # VideoCapture 객체를 메모리 해제하고 모든 윈도우 창을 종료합니다.
# cap.release()
# cv.destroyAllWindows()
