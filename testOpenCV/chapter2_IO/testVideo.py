# -*- coding: UTF-8 -*-
import cv2
import numpy as np

videoCapture = cv2.VideoCapture('./video/Megamind.avi')

fps = videoCapture.get(cv2.CAP_PROP_FPS)

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter("../videoResult/MyOutputVid1.avi", cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)

success, frame = videoCapture.read()

while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()

videoCapture.release()

