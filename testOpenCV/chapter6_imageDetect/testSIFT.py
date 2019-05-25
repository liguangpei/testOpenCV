import cv2
import numpy as np
import sys

#由于算法专利问题，SIFT算法没有自带进opencv，需要使用cmake编译
img = cv2.imread("../img/chess_board3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
myKeyPoints, descriptor = sift.detectAndCompute(gray, None)
cv2.drawKeypoints(img, myKeyPoints, img, (0,255,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('sift_keypoints', img)

while True:
    if cv2.waitKey(1000//12) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

