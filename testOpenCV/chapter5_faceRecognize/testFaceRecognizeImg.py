import cv2

OPENCV_PATH = r"C:/Python/Python37/Lib/site-packages/cv2/data/"
face_cascade = cv2.CascadeClassifier(OPENCV_PATH + 'haarcascade_frontalface_default.xml')

img = cv2.imread('../img/messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 2)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w,y+h), (0, 0, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()