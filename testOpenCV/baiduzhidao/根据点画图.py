# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
points = ((0,0),(1,0),(0,1),(1,2),(0,3))
x = []
y = []
xmin = 0
ymin = 0
xmax = 0
ymax = 0
for point in points:
    x.append(point[0])
    y.append(point[1])
    if point[0]<xmin:
        xmin = point[0]
    if point[0] > xmax:
        xmax = point[0]
    if point[1] < ymin:
        ymin = point[1]
    if point[1] > ymax:
        ymax = point[1]

fig = plt.figure()# 创建图
ax = fig.add_subplot(1,1,1)
ax.plot(x, y, 'ko')#x=[1,2,3,4],y=[1,4,9,16],'ro'表示红色的圆点

#axis接收的list参数表示：[xmin, xmax, ymin, ymax]

ax.axis([xmin-2, xmax+2, ymin-2, ymax+2])#设置x、y轴的长度，x轴为[0,6],y轴为[0,20]

width = xmax-xmin
height = ymax-ymin
top = ymax
left = xmin
print(left, top, width, height)
ax.add_patch(plt.Rectangle((xmin,ymin),width,height,fill=False))

for ix in range(xmin, xmax+1):
    for iy in range(ymin, ymax+1):
        point = (ix, iy)
        if point in points:
            pass
        else:
            cir1 = Circle( xy=point, radius=0.1, alpha=0.5)
            ax.add_patch(cir1)

plt.show()