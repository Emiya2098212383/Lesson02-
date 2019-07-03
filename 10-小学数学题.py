# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Steven Lu

# 目的:
# 写第一套程序
import random

# 打印开头
# print("---开始出题目---")
# 卷子部分
filename = "小学数学卷.txt"
f = open(filename,"w") # write 方式第一次写一行
text2write = "---开始出题目---\n"
f.write(text2write)
f.close()

#答案部分
file2 = "小学数学卷及其答案.txt"
f2 = open(file2, "w")
line2 = "小学数学卷的答案 \n"
f2.write(line2)

# 用"a"方式打开，准备追加答案
# 指定文件名
filename = "小学数学卷.txt"

# 开始追加内容
f = open(filename,"a")
print("----小学四则运算题----")

count=0

#for i in range(1,100):
    #count=count+1
for row in range(1,21):
    line1= ''
    line2= ''
    for col in range(1,6):
        count =count + 1
        anwser = 0

        a = random.randint(1, 100)
        b = random.randint(1, 100)

        op = random.randint(1, 4)
        #当op=4 时是加法
        if op == 1:
            line1 = line1 + "%d + %d = \t" % (a, b)
            anwser = a + b
            line2 = line2 + "%d + %d = %d \t\t\t" % (a, b, anwser)

        #当op=4 时是减法
        if op == 2:
            line1 = line1 + "%d - %d = \t" % (a, b)
            anwser = a - b
            line2 = line2 + "%d - %d = %d \t\t\t" % (a, b, anwser)

        #当op=4 时是乘法
        if op == 3:
            line1 = line1 + "%d × %d = \t" % (a, b)
            anwser = a * b
            line2 = line2 + "%d × %d = %d \t\t\t" % (a, b, anwser)

        #当op=4 时是除法
        if op == 4:
            line1 = line1 + "%d ÷ %d = \t" % (a, b)
            anwser = a / b
            line2 = line2 + "%d ÷ %d = %0.3f \t\t\t" % (a, b, anwser)

        # print('现在打印第{0}行-第{1}列-第{2}道数学题'.format(row,col,count))
    text2write = line1 + "\n"
    f.write(text2write)

    line2 = line2 + "\n"
    f2.write(line2)

text2write = "---总共出了{0}道四则运算题---\n".format(count)
f.write(text2write)
line2 = "---总共出了{0}道四则运算题---以上含答案---\n".format(count)
f2.write(line2)

#最后关闭
f.close()
f2.close()
