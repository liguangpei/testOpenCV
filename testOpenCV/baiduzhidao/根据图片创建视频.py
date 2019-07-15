#-*- coding: UTF-8 -*-
import os
import numpy as np
import cv2
# import matplotlib.pyplot as plt
import os

IMG_WIDTH = 2304
IMG_HEIGHT = 2940
ANGLE_CNT = 360

ROI_WIDTH = 1536
ROI_HEIGHT = 1920

"""
def cvt16to8(inputfileName):
    tmpimg = cv2.imread(inputfileName, cv2.IMREAD_ANYDEPTH)
    newImg = np.zeros((ROI_HEIGHT,ROI_WIDTH), dtype=np.uint8)
    for row in range(ROI_HEIGHT):
        for col in range(ROI_WIDTH):
            newImg[row,col] = tmpimg[row,col]%255
    return newImg
"""


input_file_path = "D:/XTray3DImgSoft/CLTest/20190706_110kv_5w_5frame/ave_roi_raw/"
input_file_basis_name = "proj_%d.raw"
# 创建视频文件
#先调用构造函数确定文件的名称，格式，帧率，帧大小，是否彩色。其中格式作为第二个参数，
"""
fourcc为 四个字符用来表示压缩帧的codec 
例如：
CV_FOURCC('P','I','M','1') = MPEG-1 
codecCV_FOURCC('M','J','P','G') = motion-jpeg 
codecCV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 
codecCV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 
codecCV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 
codecCV_FOURCC('U', '2', '6', '3') = H263 
codecCV_FOURCC('I', '2', '6', '3') = H263I 
codecCV_FOURCC('F', 'L', 'V', '1') = FLV1 codec
"""
fps = 25
size = (1536, 1920)
writer = cv2.VideoWriter("VideoTest1.avi", cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)

# start the processing
#def saveImgToVideo(writer):
for ang_idx in range(ANGLE_CNT):
    #ang_idx = 0 #单帧图像测试
    print("current angle: ", ang_idx)
    input_file_name = input_file_path+input_file_basis_name % ang_idx
    print(input_file_name)

    #由于存的raw是16位的，所以dtype=np.uint16
    img = np.fromfile(input_file_name, dtype=np.uint16)
    #转成图像数组
    img = img.reshape(ROI_HEIGHT, ROI_WIDTH)
    #转成float32类型
    img = np.float32(img)

    #获得图像最大值和最小值
    #imax = np.max(img)
    #imin = np.min(img)
    #print(imax, imin)
    #做一个中值滤波，去掉最大值和最小值
    img = cv2.medianBlur(img, 3)

    #imax = np.max(img)
    #imin = np.min(img)
    #print(imax, imin)

    imax = min(np.max(img)+200, 16384)
    imin = max(np.min(img)-200, 0)

    alpha = 255 / (imax-imin)
    beta = imin * 255 / (imin-imax)
    #img1 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)#效果同下面2行代码
    img1 = alpha * img + beta
    img1 = np.uint8(img1)

    #img1.tofile("result.raw")
    #print(img1.shape)#(1920, 1536)


    #一下三句代码用于存成3通道的jpg图像
    #cv2.imwrite("test.jpg", img1)
    #img1 = cv2.imread("test.jpg")
    #print(img1.shape)#(1920, 1536, 3)
    #将单通道转成3通道图片才能存到视频中
    img1 = np.expand_dims(img1, axis=2)
    img1 = np.concatenate((img1, img1, img1), axis=-1)
    print("newShape:",img1.shape)
    cv2.imshow("img", img1)
    writer.write(img1)
    cv2.waitKey(50)
print("end")
writer.release()
cv2.waitKey(0)
cv2.destroyAllWindows()



