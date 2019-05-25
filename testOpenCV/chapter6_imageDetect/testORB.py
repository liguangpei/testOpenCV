import cv2
import numpy as np
from matplotlib import pyplot as plt

#  读取图片
img1 = cv2.imread('../img/mylogo.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../img/mycontainlogo.png', cv2.IMREAD_GRAYSCALE)

#  创建ORB，并执行检测
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

#  创建暴力匹配对象，执行匹配
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
#  排序
matches = sorted(matches, key=lambda x: x.distance)
#  画出匹配线
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:40], img2, flags=2)
plt.imshow(img3)
plt.show()
