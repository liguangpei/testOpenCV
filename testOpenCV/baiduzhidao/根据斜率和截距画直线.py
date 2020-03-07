# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#生成x的等差数列0-10之间取100个数
x = np.linspace(0,10, 10)
print(x)
z = x.reshape(-1, 1)
print(z)
#生成每个x对应的y
y = 0.5*x+3
#画直线
plt.plot(x, y, c='orange')
#画标题
plt.title("y=0.5x+3")
#显示
plt.show()



