# -*- coding: UTF-8 -*-
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
plt.cm.get_cmap()
lr = LinearRegression()
lr.coef_