# -*- coding: UTF-8 -*-
import cv2

"""
此文件用于显示摄像头帧图像
onMyMouse鼠标处理消息函数
"""
clicked = False


def onMyMouse(event, x, y, flags, param):

    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


videoCapture = cv2.VideoCapture(0)  # 摄像头索引

cv2.namedWindow("MyWindow")
cv2.setMouseCallback('MyWindow', onMyMouse)

success, frame = videoCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow("MyWindow", frame)
    success, frame = videoCapture.read()

cv2.destroyWindow("MyWindow")
videoCapture.release()
