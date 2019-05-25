# -*- coding: UTF-8 -*-

"""
要求用递归、递推和Lambda三种方式编写power(n,x)函数
"""
#递归
def power(n, x):
    if abs(1/pow(n, x))<abs(pow(10, -2)):
        return 0#回归条件
    else:
        m = n + 1#递归因子
        if(n%2==1):
            return 1/pow(n, x)+power(m, x)#求和奇正
        else:
            return -1/pow(n, x)+power(m, x)#求和偶负

def power2(n, x):
    sum = 0
    while(1/pow(n,x)>abs(pow(10, -2))):
        if (n % 2 == 1):
            sum+= 1 / pow(n, x)
        else:
            sum+=-1 / pow(n, x)
        n += 1  # 递增
    return sum

if __name__ == "__main__":
    x = input("请输入幂数")
    x = int(x)
    n = 1
    sum = power(n, x)
    print(sum)
    n=1
    sum = power2(n, x)
    print(sum)
