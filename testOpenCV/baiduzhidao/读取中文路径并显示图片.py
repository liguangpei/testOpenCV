#-*- coding: UTF-8 -*-

import os
import glob
import cv2
import numpy as np

def cv_imread(filename):
    cv_img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8),-1)
    return cv_img

path = "C:/Users/CL/Pictures/CL_Camera_img/"
for filename in os.listdir(path):
    if filename.endswith("png") or filename.endswith("PNG"):
        print (filename)
        filename = path+filename
        #img = cv2.imread(filename)
        img = cv_imread(filename)
        cv2.imshow("img", img)
        cv2.waitKey(500)
print("averaging finished!\n")
#cv2.waitKey(0)
cv2.destroyAllWindows()