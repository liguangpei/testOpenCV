# -*- coding: UTF-8 -*-
import cv2

#此处不支持中文
img = cv2.imread(r"../img/pro.png")
cv2.imshow("1", img)
cv2.waitKey(0)
#释放窗口
cv2.destroyAllWindows()