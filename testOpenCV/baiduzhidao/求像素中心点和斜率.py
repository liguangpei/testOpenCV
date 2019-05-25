# -*- coding: UTF-8 -*-
import numpy as np
import cv2
"""
#创建一张图512*512 3通道
width = 512
height = 512
channel = 3
img = np.zeros(shape=[width, height, channel], dtype=np.uint8)

# 遍历每个像素点，并进行赋值
for i in range(width):
    for j in range(height):
        if i==width//2 and j==height//2:
            img[i,j,:]=[255,255,255]
        else:
            img[i,j,:]=[0,0,0]
# 展示图片
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow('img', img)
"""
#解题思路：因为我下载的你的图片，黑色周围还有白色，所以先去除了周围的白色，保证只有黑色部分图片
#对图片转灰度图，这样方便计算，每个像素点的值就是一个0-255的值，0为黑色，255为白色
#然后获得灰度图的row和col，与正常思维的width和height相反，row对应height，col对应width
#遍历row和col，先获得第一个白点，再获得最后一个白点，然后根据这两个坐标执行tan计算斜率k值
#读取图像
img2 = cv2.imread("../img/blackWhite.png")
#转成单通道黑白图
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('img2', img2)
cv2.imshow('gray', gray)

sp = gray.shape
rows = sp[0]
cols = sp[1]
cr = 0
cl = 0
#裁剪左边和上边空白
for row in range(rows):
    isBreak = False
    for col in range(cols):
        if gray[row, col]==0:
            cr = row
            cl = col
            print("\nrow=%d,col=%d"%(row, col))
            isBreak = True
            break
        #print(gray[row, col], end='')
        #if(col==cols-1):
            #print("\nrow=%d,col=%d-------------------------------"%(row, col))
    if isBreak==True:
        break
print (cr, cl, rows, cols, rows-cr, cols-cl)
gray2 = gray[cr:rows-cr, cl:cols-cl]
cv2.imshow('gray2', gray2)

#裁剪右下角空白
sp = gray2.shape
rows = sp[0]
cols = sp[1]
row = rows-1

print ("gray2 crop:", rows, cols, row, col)
while row!=0:
    isBreak = False
    col = cols - 1
    while col!=0:
        if gray2[row,col]==0:
            isBreak = True
            break
        col-=1
    if isBreak==True:
        break
    row-=1
gray3 = gray2[0:row+1, 0:col+1]
cv2.imshow('gray3', gray3)

#对裁剪后的gray3求中心点坐标
sp = gray3.shape
rows = sp[0]
cols = sp[1]
x = cols//2
y = rows//2
print("中心点坐标(%d,%d),图片宽高(w=%d, h=%d)"%(x,y,cols,rows))

#求斜率 (y2-y1)/(x2-x1)
#遍历出第一个白点和最后一个白点，做计算
x1y1=[]
x2y2=[]

#求第一个白点坐标
for row in range(rows):
    isBreak = False
    for col in range(cols):
        if gray3[row,col]==255:
            x1y1.append(col)
            x1y1.append(row)
            isBreak = True
            break
    if isBreak==True:
        break
#求最后一个白点坐标
row = rows-1
while row!=0:
    isBreak = False
    col = cols - 1
    while col!=0:
        if gray2[row,col]==255:
            x2y2.append(col)
            x2y2.append(row)
            isBreak = True
            break
        col-=1
    if isBreak==True:
        break
    row-=1
print(x1y1,x2y2)
#计算斜率tan值
k = abs(x2y2[1]-x1y1[1])/abs(x2y2[0]-x1y1[0])
print("斜率k=",k)
cv2.waitKey(0)
cv2.destroyAllWindows()