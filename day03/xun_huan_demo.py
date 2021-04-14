# # # !/usr/bin/env python
# # -*-coding:utf-8 -*-
#
# """
# # File       : xun_huan_demo.py
# # Time       ：2021/4/8 11:31
# # Author     ：taoyong
# # version    ：python 3.7
# """
#
# # for 循环
# """
# 字符串 list tuple dict set
# for 循环变量 in 可迭代对象
#     循环体
# """
#
# for i in [1, 2, 3, 4, 5, 6, 7]:
#     print(i)
# '''
# range(第一个参数，第二个参数，第三个参数)
#
# 第一个参数:迭代起始的数据，默认值0
# 第二个参数：迭代截至的数据，开区间
# 第三个参数：增量，可正可负，默认值为1
# '''
#
# for i in range(10):
#     print(i)
#
# l = [1, 2, 3, 4, 5, 6, 7]
# for i in range(6):
#     print(l[i])
#
# t = [1, 2, 3, 4, 5, 6, 7]
# for i in range(6):
#     print(t[i])
#
# for i in {1, 2, 3, 4, 5, 6}:
#     print(i)
#
# d = {"name": "小明", "age": 18, "sex": "男"}
# for k in d:
#     print(d[k])
#
# # while 循环
# '''
# while 条件 ：
#     循环体
# '''
# i = 10
# while i > 1:
#     print(i)
#     i -= 1
#
# '''
# l = [1, 2, 3, 4, 5, 6, 7]
# for i in range(6):
#     print(l[i])
# 上边代码改成while循环
# '''
# l = [1, 2, 3, 4, 5, 6, 7]
# i = 0
# while i < 7:
#     print(l[i])
#     i += 1
#
# # 求出1+2+3+。。。。+100的和  sum 求和
#
# l = 0
# i = 1
# while i <= 100:
#     l = l + i
#     i += 1
# print(l)
#
# # 找到列表[1,2,3,4,5,6,7,8,9]中7的下标
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 7
#
# for i in range(len(l)):  # len ()求出元素的个数
#     if l[i] == target:  # 判断列表中当前位置的值是否和目标相等
#         print(i)  # 如果相等，打印出下标
#         break  # 中止当前循环
#
# # 打印出1-100以内，可以被3整数的数
# for i in range(1, 101):
#     if i % 3 != 0:
#         continue  # 跳过本次循环
#     print(i)
#
# # 九九乘法表
# for i in range(1, 10):  # i代表行
#     for j in range(1, i + 1):  # j代表列
#         print("{}x{}={}\t".format(j, i, i * j), end="")
#     print()


# 冒泡排序
l = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
length = len(l)
for i in range(length):
    for j in range(length - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)

# 100以内的质数
for i in range(2, 100):
    flag = True  # True 代表是质数
    for j in range(2, i):
        if i % j == 0:
            flag = True  # False代表不是质数
            # print（"{}不是质数"，format(i)）
            break
    if flag:
        print(i)
