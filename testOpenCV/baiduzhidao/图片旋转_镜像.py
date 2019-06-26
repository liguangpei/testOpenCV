# -*- coding: UTF-8 -*-
import cv2
import numpy as np

#图像旋转函数
def rotate_bound(image, angle):
    #计算图像中心坐标
    (h, w) = image.shape[:2]
    (cx, cy) = (w//2, h//2)

    #计算旋转矩阵
    M = cv2.getRotationMatrix2D((cx, cy), -angle, 1.0)
    print(M)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])

    #计算旋转后的宽高
    nW = int(h*sin+w*cos)
    nH = int(h*cos+w*sin)

    #调整旋转矩阵中心偏移量
    M[0,2]+=(nW/2)-cx
    M[1,2]+=(nH/2)-cy

    return cv2.warpAffine(image, M, (nW, nH))

img = cv2.imread("../img/1.jpg")
rotatedImg = rotate_bound(img, 90)
cv2.imshow("srcImg", img)
cv2.imshow("rotatedImg", rotatedImg)

#上下翻转，沿着X轴镜像
imgH = cv2.flip(img, 0)
cv2.imshow("imgH", imgH)
#左右翻转，沿着Y轴镜像
imgV = cv2.flip(img, 1)
cv2.imshow("imgV", imgV)
#上下左右翻转
imgN = cv2.flip(img, -1)
cv2.imshow("imgN", imgN)



cv2.waitKey()
cv2.destroyAllWindows()