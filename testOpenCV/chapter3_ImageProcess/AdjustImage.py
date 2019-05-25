from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

ANSWER_KEY = {0:1,1:4,2:0,3:3,4:1}

image = cv2.imread("test2.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("test2_gray.jpg", gray)
blurred = cv2.GaussianBlur(gray, (3,3),0)
cv2.imwrite("test2_blurred.jpg", blurred)
edged = cv2.Canny(blurred,75,200)
cv2.imwrite("test2_edged.jpg", edged)
cnts,hier = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
'''
if imutils.is_cv2():
    print("111")
    cnts = cnts[0]
else:
    print("222")
    cnts = cnts[1]
'''
docCnt =None

if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    print("len:%d" % len(cnts))
    i = 0
    for c in cnts:
        peri = cv2.arcLength(c, True)
        print("peri:",peri)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        print("len(approx):",len(approx))
        if len(approx) == 4:
            docCnt = approx
            paper = four_point_transform(image, docCnt.reshape(4, 2))
            warped = four_point_transform(gray, docCnt.reshape(4, 2))
            # cv2.imshow("original", image)
            # cv2.imshow("Exam", paper)

            cv2.imwrite("test2_image%d.jpg" % (i,), image)
            cv2.imwrite("test2_paper%d.jpg" % (i,), paper)
            cv2.imwrite("test2_warped%d.jpg" % (i,), warped)
            i+=1
            continue


cv2.waitKey(0)