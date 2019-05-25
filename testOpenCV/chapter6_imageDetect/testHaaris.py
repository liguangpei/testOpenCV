import cv2
import numpy as np

#  读取图像文件，并转为灰度图像，准备计算
img = cv2.imread('../img/chess_board3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#  对灰度图执行角点检测算法
dst = cv2.cornerHarris(gray, 2, 23, 0.04)  #23定义了检测角点的敏感度，取值范围3-31的奇数
img[dst > 0.01 * dst.max()] = [0, 0, 255]  #将检测到的角点标记为红色
while True:
    cv2.imshow("corners", img)
    if cv2.waitKey(1000 // 12) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
