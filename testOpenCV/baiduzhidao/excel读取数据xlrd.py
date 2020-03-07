# -*- coding: UTF-8 -*-

import xlrd
import os

filename = "data2.xlsx"
filePath = os.path.join(os.getcwd(), filename)
x1 = xlrd.open_workbook(filePath)
# 2、获取sheet对象
print ('sheet_names:', x1.sheet_names())  # 获取所有sheet名字
print ('sheet_number:', x1.nsheets)        # 获取sheet数量
print ('sheet_object:', x1.sheets())       # 获取所有sheet对象
#print ('By_name:', x1.sheet_by_name("test"))  # 通过sheet名查找
print ('By_index:', x1.sheet_by_index(0))  # 通过索引查找

"""
4、获取sheet的汇总数据：
获取sheet名：sheet1.name
获取总行数：sheet1.nrows
获取总列数：sheet1.ncols
"""
# 获取sheet的汇总数据
sheet1 = x1.sheet_by_index(0)
print ("sheet name:", sheet1.name)   # get sheet name
print ("row num:", sheet1.nrows)  # get sheet all rows number
print ("col num:", sheet1.ncols)  # get sheet all columns number
""""
# 单元格批量读取
print(sheet1.row_values(0))  # 获取第一行所有内容，合并单元格，首行显示值，其它为空。
print (sheet1.row(0))         # 获取单元格值类型和内容
print( sheet1.row_types(0))   # 获取单元格数据类型
"""

# 特定单元格读取
# 取值
#print (sheet1.cell_value(1, 1))
print (sheet1.cell(1, 0).value)
#print (sheet1.row(1)[1].value)

#取类型
#print (sheet1.cell(1, 1).ctype)
print (sheet1.cell_type(1, 0))
#print (sheet1.row(1)[1].ctype)


import matplotlib.pyplot as plt
import numpy as np

rows = sheet1.nrows
cols = sheet1.ncols
x = range(0, rows)
x1=[]
x2=[]
y1 = []
y2 = []
for i in range(0, rows):
    if i%1==0:
        x1.append(i)
        x2.append(i)
        print(i)
        y1.append(float(sheet1.cell(i, 0).value))
        y2.append(float(sheet1.cell(i, cols-1).value))

fig = plt.figure(figsize=(20,12),dpi=80)
ax1=fig.add_subplot(1, 2, 1)##左右布局
plt.sca(ax1)
plt.title('Result Analysis')
plt.plot(x1, y1,label="col1",color="#DB7093", marker='*')
plt.legend() # 显示图例
plt.xlabel('data seq')
plt.ylabel('data value')

ax2=fig.add_subplot(1, 2, 2)##左右布局
plt.sca(ax2)
plt.title('Result Analysis')
plt.plot(x2, y2, label="col3",color="#F08080", marker='*')
plt.legend() # 显示图例
plt.xlabel('data seq')
plt.ylabel('data value')

plt.show()