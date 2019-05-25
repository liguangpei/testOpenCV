# -*- coding: UTF-8 -*-
"""
摄像头捕获10秒视频
5种视频格式
未压缩的YUV颜色编码:I 4 2 0
MPEG-1:P I M 1
MPEG-4:X V I D
OGV: T H E O
Flash: F L V 1
"""
import cv2


videoCapture = cv2.VideoCapture(0)#摄像头索引

fps = 30#默认捕获帧率

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))#每帧大小

videoWriter = cv2.VideoWriter("../videoResult/MyOutputCameraVideo.avi", cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)

success, frame = videoCapture.read()
numFrameRemaining = 10 * fps - 1

while success and numFrameRemaining>0 :
    videoWriter.write(frame)
    success, frame = videoCapture.read()
    numFrameRemaining -= 1

videoCapture.release()

