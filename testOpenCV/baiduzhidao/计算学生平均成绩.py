# -*- coding: UTF-8 -*-

class student:
    # 构造函数
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.mapCourseGrade={}

    def setCourseGrade(self, courses, grades):
        for i in range(len(courses)):
            course = courses[i]
            grade = grades[i]
            self.mapCourseGrade[course] = grade

    def getAverageGrade(self):
        sum = 0
        for key in self.mapCourseGrade.keys():
            sum+=self.mapCourseGrade[key]
        sum/=len(self.mapCourseGrade)
        return sum

if __name__ == "__main__":
    a = student("兰兰", "1000")
    b = student("啊珍", "1001")
    c = student("小红", "1002")

    a.setCourseGrade(["计算机导论", "算法导论","离散数学"], [98,97,90])
    b.setCourseGrade(["计算机导论", "离散数学", "数据结构"], [91, 80, 93])
    c.setCourseGrade(["操作系统", "算法导论", "计算机网络"], [90, 89, 78])

    print("%s,%s,%d"%(a.name, a.number, a.getAverageGrade()))
    print("%s,%s,%d"%(b.name, b.number, b.getAverageGrade()))
    print("%s,%s,%d" % (c.name, c.number, c.getAverageGrade()))
