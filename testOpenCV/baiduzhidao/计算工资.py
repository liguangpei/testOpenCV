# -*- coding: UTF-8 -*-
import numpy

salary = 20500 #每月工资数
totalMonth = 12 #工资总月数
freeMoney = 5000 #个税免费基数
freeOther = 2000 #每月扣除数，房租或养老
rate_sb = 0.12
rate_gjj = 0.08
rate_total = rate_sb+rate_gjj

needPayRate = 0.0#缴税税率
needMinus = 0.0 #速算扣除数
maxMoney = 0#总到手
maxMoneyNoGJJ = 0#总到手不含公积金
maxValue1 = 0#最合适的社保基数
maxValue2 = 0#最合适的社保基数2（总到手不含公积金）

totalSalary = salary*totalMonth #总工资
totalFreeMoney = freeMoney*totalMonth #总免费基数
totalFreeOther = freeOther*totalMonth #总的其他数
print("总工资:%.2f, 总免税:%.2f, 总扣除：%.2f"%(totalSalary, totalFreeMoney, totalFreeOther))
for sb in range(5000, 17000, 1000):
    totalSB = sb*rate_total*totalMonth #总社保公积金数
    totalNeedPay = totalSalary-totalFreeMoney-totalFreeOther-totalSB #需要缴税总额
    if(totalNeedPay>0 and totalNeedPay<36000):
        needPayRate = 0.03
        needMinus = 0
    elif(totalNeedPay>36000 and totalNeedPay<=144000):
        needPayRate = 0.1
        needMinus = 2520
    elif(totalNeedPay>144000 and totalNeedPay<=300000):
        needPayRate = 0.2
        needMinus = 16920
    totalTax = totalNeedPay*needPayRate-needMinus#总税额
    total_sb = sb*rate_sb*totalMonth #总社保额
    total_gjj = sb*rate_gjj*totalMonth*2 #总公积金
    totalGetMoney = totalSalary-total_sb-totalTax+total_gjj #获得总数
    totalGetMoneyNoGJJ = totalSalary-totalSB-totalTax #获得不带公积金和社保的总数
    totalGSNeedPay = sb*rate_sb*totalMonth*2+sb*rate_gjj*totalMonth
    totalGSNeedPayAll = totalGSNeedPay+totalSalary

    if maxMoney<totalGetMoney:
        maxMoney = totalGetMoney
        maxValue1 = sb
    if maxMoneyNoGJJ<totalGetMoneyNoGJJ:
        maxMoneyNoGJJ = totalGetMoneyNoGJJ
        maxValue2 = sb
    print("社保基数:%10.2f,总社保公积金:%.2f, 缴税总额:%.2f, 总缴税:%.2f,总公积金:%10.2f, 总到手:%.2f, 总到手不含公积金:%.2f, 公司付出的社保和公积金:%.2f,公司总付出:%.2f"
          %(sb, totalSB, totalNeedPay, totalTax, total_gjj, totalGetMoney, totalGetMoneyNoGJJ, totalGSNeedPay,totalGSNeedPayAll))


print("maxMoney=%.2f, maxValue1=%.2f, maxMoneyNoGJJ=%.2f, maxValue2=%.2f"%(maxMoney, maxValue1, maxMoneyNoGJJ, maxValue2))