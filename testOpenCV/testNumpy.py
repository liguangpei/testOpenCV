# -*- coding: UTF-8 -*-
import numpy as np

print(np.eye(3))
print("----------------------")
print(np.eye(4))
print("----------------------")
print(np.eye(5))

a = np.array([1, 2, 3, 4, 5])

# 保存到 outfile.npy 文件上
np.save('outfile.npy', a)