# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : var_set.py
# Time       ：2021/4/7 16:38
# Author     ：taoyong
# version    ：python 3.7
"""
# 创建 set

# 为空
s = set()
print(s)

# 有值
s = {1, 2, 3, 4}
print(s)

# 或者
s = set([1, 2, 3, 4])
print(s)

# 子集
s1 = {1, 2, 3, 4, 5, 6}
s2 = {2, 3, 4}
print(s1 > s2)  # s2不在s1中，返回True

s1 = {1, 2, 3, 4, 5, 6}
s2 = {2, 3, 4, 9}
print(s1 > s2)  # s2不在s1中，返回False

# 交集
s1 = {1, 2, 3, 4, 5, 6}
s2 = {2, 3, 4}
print(s1 & s2)  # s1和s2的交集

# 并集
s1 = {1, 2, 3, 4, 5, 6}
s2 = {2, 3, 4}
print(s1 | s2)  # s1和s2的并集

# 差集
s1 = {1, 2, 3, 4, 5, 6}
s2 = {2, 3, 4}
print(s1 - s2)  # s1中存在，但是在s2中不存在的元素
