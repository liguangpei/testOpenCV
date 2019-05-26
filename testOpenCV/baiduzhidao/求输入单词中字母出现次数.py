# -*- coding: UTF-8 -*-

#简历一个字典，key=26个英文字母，value为出现次数
wordDict = {}
#获得输入单词字符串
str = input("请输入一串单词")
#用空格分割单词，存到列表
strArr = str.split(sep=' ')
#遍历列表中的单词
for word in strArr:
    #遍历单词中的字母
    for ch in word:
        #判断字典中是否存在键key
        if ch in wordDict:
            wordDict[ch] = wordDict.get(ch)+1#计数+1
        else:
            wordDict[ch] = 1#计数初始化为1

#打印输出
for key,value in wordDict.items():
    print("%s=%d"%(key, value))