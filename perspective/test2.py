import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
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
    img_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    cv2.imshow('img', img)
    # cv2.imshow('result', result)
    height, width = img_gray.shape[:2]

    img_gray = cv2.resize(img_gray, (2*width, 2*height), interpolation = cv2.INTER_CUBIC )
    cv2.imshow('img_gray', img_gray)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
