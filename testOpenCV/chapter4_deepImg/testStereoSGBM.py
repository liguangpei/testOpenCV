import cv2
import numpy as np
from matplotlib import pyplot as plt


def update(val = 0):
    stereo.setBlockSize(cv2.getTrackbarPos('window_size', 'disparity'))
    stereo.setUniquenessRatio(cv2.getTrackbarPos('uniquenessRatio','disparity'))
    stereo.setSpeckleWindowSize(cv2.getTrackbarPos('speckleWindowSize','disparity'))
    stereo.setSpeckleRange(cv2.getTrackbarPos('speckleRange','disparity'))
    stereo.setDisp12MaxDiff(cv2.getTrackbarPos('disp12MaxDiff','disparity'))

    print('computing disparity...')
    disp = stereo.compute(imgL, imgR)#.astype(np.float32)/16.0
    #cv2.imshow('left', imgL)
    #cv2.imshow('disparity', disp)
    plt.subplot(121), plt.imshow(imgL, 'gray'), plt.title('img_left'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(disp, 'gray'), plt.title('disparity'), plt.xticks([]), plt.yticks([])
    plt.show()



if __name__ == '__main__':
    window_size = 5
    min_disp = 16
    num_disp = 192-min_disp
    blockSize = window_size
    uniquenessRatio = 1
    speckleRange = 2
    speckleWindowSize = 3
    disp12MaxDiff = 200

    P1 = 600
    P2 = 2400

    imgL = cv2.imread('../img/imgLeft.jpg')
    imgR = cv2.imread('../img/imgRight.jpg')

    cv2.namedWindow('disparity')
    cv2.createTrackbar('speckleRange', 'disparity', speckleRange, 50, update)
    cv2.createTrackbar('window_size', 'disparity', window_size, 21, update)
    cv2.createTrackbar('speckleWindowSize', 'disparity', speckleWindowSize, 200, update)
    cv2.createTrackbar('uniquenessRatio', 'disparity', uniquenessRatio, 50, update)
    cv2.createTrackbar('disp12MaxDiff', 'disparity', disp12MaxDiff, 250, update)

    stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
                                   numDisparities=num_disp,
                                   blockSize=blockSize,
                                   P1=P1, P2=P2,
                                   disp12MaxDiff=disp12MaxDiff,
                                   uniquenessRatio=uniquenessRatio,
                                   speckleWindowSize=speckleWindowSize,
                                   speckleRange=speckleRange)
    update()
    cv2.waitKey()


