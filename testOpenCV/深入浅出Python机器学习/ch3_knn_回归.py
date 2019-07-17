# -*- coding: UTF-8 -*-
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
#导入用于回归分析的knn模型
from sklearn.neighbors import KNeighborsRegressor
#导入数据集,生成特征数量为1，噪音为50的数据集
X, y = datasets.make_regression(n_samples=100, n_features=1, n_informative=1, noise=50, random_state=8)
#用三点图可视化数据
#plt.scatter(X, y, c='orange', edgecolors='k')
#plt.show()

reg = KNeighborsRegressor()
#用knn模型拟合数据
reg.fit(X, y)

#把预测结果用图像可视化
z = np.linspace(-3, 3, 200).reshape(-1, 1)
plt.scatter(X, y, c='orange', edgecolors='k')
plt.plot(z, reg.predict(z), c='b', linewidth=3)
plt.title('KNN Regressor')
plt.show()

