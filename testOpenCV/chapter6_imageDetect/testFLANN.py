import cv2
import numpy as np
from matplotlib import pyplot as plt

#  读取图片
img1 = cv2.imread('../img/mylogo.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../img/mycontainlogo.png', cv2.IMREAD_GRAYSCALE)

#  创建SIFT，并执行检测
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)


#  flann算法参数
FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
searchParams = dict(checks=50) #  或者参数为空

#  创建暴力匹配对象，执行匹配
flann = cv2.FlannBasedMatcher(indexParams, searchParams)
matches = flann.knnMatch(des1, des2, k=2)

#  准备一个空的mask用来画好的匹配
matchesMask = [[0, 0] for i in range(len(matches))]
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i] = [1, 0]

drawParams = dict(matchColor=(0, 255, 0),
                  singlePointColor=(255, 0, 0),
                  matchesMask=matchesMask,
                  flags=0)

resultImage = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **drawParams)

#  画出匹配线
plt.imshow(resultImage)
plt.show()