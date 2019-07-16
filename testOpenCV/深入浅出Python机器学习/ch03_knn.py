# -*- coding: UTF-8 -*-
#导入数据集生成器
from sklearn.datasets import make_blobs
#导入knn分类器
from sklearn.neighbors import KNeighborsClassifier
#导入画图工具
import matplotlib.pyplot as plt
#导入数据拆分工具
from sklearn.model_selection import train_test_split
import  numpy as np

#生成样本数为200，分类为2的数据集
data = make_blobs(n_samples=20, centers=2, random_state=8)
x,y=data
print(x.shape)
print(x)
#print(y)
#将生成的数据集进行可视化显示
#plt.scatter(x[:,0], x[:,1], c=y, cmap=plt.cm.get_cmap('spring'), edgecolors='k')
#plt.show()

"""
cmaps = [('Perceptually Uniform Sequential', [
            'viridis', 'plasma', 'inferno', 'magma']),
         ('Sequential', [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         ('Sequential (2)', [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']),
         ('Diverging', [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ('Miscellaneous', [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]
"""

clf = KNeighborsClassifier()
clf.fit(x,y)

#下面的代码用于画图
x_min, x_max = x[:,0].min()-1, x[:,0].max()+1
y_min, y_max = x[:,1].min()-1, x[:, 1].max()+1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
plt.pcolormesh(xx, yy, z, cmap=plt.cm.get_cmap('Pastel1'))
plt.scatter(x[:,0], x[:, 1], c = y, cmap=plt.cm.get_cmap('spring'), edgecolors='w')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Classifier:KNN")
#把新的数据点用红五星表示
newpoint = [6.75, 4.82]
plt.scatter(newpoint[0],newpoint[1], marker='*', c='red', s=200)
#对新数据点分类进行判断
print('\n\n\n')
print('===============================================')
print('新数据点分类是:',clf.predict([newpoint]))
print('===============================================')
print('\n\n\n')
plt.show()