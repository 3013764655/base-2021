# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Fite       : var_tupte.py
# Time       ：2021/4/7 15:26
# Author     ：taoyong
# version    ：python 3.7
"""
t = [1, 2, 3, 4, 5, 6, "a", "v", "c", "b"]

# 访问列表中的指定元素
print(t[3])  # [] 取下标

# 列表截取 t[n:m]  n表示起始下标，m表示结束下标+1
# 截取下标2-8的字符
print(t[2:9])

# t[n:]  表示从下标为n的字符开始，截取到列表结尾
print(t[2:])

# t[：m]  表示从下标为0的字符开始，截取到下表为m-1的字符为止
print(t[:9])

# 下标可以为负，倒着数，从-1开始
print(t[-6: -2])

# t[n:m:step] step: 步长，默认为1
print(t[1:11:2])

# t[::step] step: 步长可为负数,从后往前截取
print(t[-2:-10:-1])

# 拼接 两个列表拼接到一起，但是两个列表本身不发生变化
t1 = "abc"
t2 = "123"
print(t1 + t2)
print(t1)
print(t2)

# 创建元组
t = (1,)  # 元组中只有一个元素 只有一个元素时需要用","分隔开
print(t)
