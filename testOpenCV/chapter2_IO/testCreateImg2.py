# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os

img = np.zeros((3,3), dtype=np.uint8)
#print(img)
print(img.shape)
#cv2.imshow("zero", img)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)
print(img.shape)
#cv2.imshow("zeroRGB", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#创建一个随机字节数组
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

#转换数组为一个400*300的灰度图像
grayImg = flatNumpyArray.reshape(300, 400)#shape默认是先列，后行
cv2.imwrite("../imgResult/randomGray.png", grayImg)

#转换数组为一个400*100的彩色图像
colorImg = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite("../imgResult/randomColor.png", colorImg)