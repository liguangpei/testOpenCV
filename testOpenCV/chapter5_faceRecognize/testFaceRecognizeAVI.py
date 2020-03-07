import sys
import cv2
import numpy as np

OPENCV_PATH = r"C:\Python37\Lib\site-packages\cv2\data/"
# Cascade classifier class for object detection.
# Python: cv2.CascadeClassifier(filename) -> CascadeClassifier object
# Parameters: filename – Name of the file from which the classifier is loaded.
face_cascade = cv2.CascadeClassifier(OPENCV_PATH + 'haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier(OPENCV_PATH + 'haarcascade_upperbody.xml')

cap = cv2.VideoCapture(r"../video/Megamind.avi")  # 打开视频文件

# Returns true if video capturing has been initialized already
if not cap.isOpened():  # 检测视频是否打开成功
    sys.exit()
#cap.set(cv2.CAP_PROP_POS_FRAMES, 30*60*35)  #设置起始帧30fps/s*60s*35min
cap.set(cv2.CAP_PROP_POS_FRAMES, 30)  #设置起始帧30fps/s*60s*35min
rate = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
delay = int(1000 / rate/4)  # 每一帧之前的延迟与视频的帧率相对应

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret!=True:
        continue
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detects objects of different sizes in the input image.
    # The detected objects are returned as a list of rectangles
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Closes video file or capturing device.
cap.release()

cv2.destroyAllWindows()
