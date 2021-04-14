# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : yun_suan.py
# Time       ：2021/4/8 10:08
# Author     ：taoyong
# version    ：python 3.7
"""

# 算术运算符
print(10 - 3)  # 减法
print(10 + 3)  # 加法
print(10 * 3)  # 乘法
print(10 / 3)  # 除法
print(10 % 3)  # 取模（取余）
print(10 // 3)  # 取整除（取商）
print(10 ** 3)  # 幂（乘方）

# 比较运算
print(1 == 1)  # 相等
print(1 != 1)  # 不相等
print(1 > 2)  # 大于
print(1 < 2)  # 小于
print(1 >= 2)  # 大于等于  False
print(1 <= 2)  # 小于等于 True

# 逻辑运算符
print(1 == 1 and 2 == 2)  # and 且 True
print(1 == 1 or 2 == 2)  # or 或 True
print(not 1 == 1)  # not 取反 False

# 成员运算符
a = "abcdefg123456789"
print("abc" in a)  # 判断"abc"是否在变量a的字符串中 True
print("abcd2" not in a)  # 判断"abcd2"是否不在变量a的字符串中 True

# 赋值运算符
a = 10  # 简单赋值运算符
a += 1  # 等价于 a = a + 1
print(a)

a = 10  # 简单赋值运算符
a -= 1  # 等价于 a = a - 1
print(a)

a = 10  # 简单赋值运算符
a *= 1  # 等价于 a = a * 2
print(a)

a = 10  # 简单赋值运算符
a /= 2  # 等价于 a = a / 2
print(a)

a = 10  # 简单赋值运算符
a %= 3  # 等价于 a = a % 3
print(a)

a = 10  # 简单赋值运算符
a //= 3  # 等价于 a = a // 3
print(a)

a = 10  # 简单赋值运算符
a **= 2  # 等价于 a = a ** 2
print(a)

# 身份运算符
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))  # id查看变量内存地址
print(id(b))  # id查看变量内存地址
print(a == b)  # 比较的是两个变量的值
print(a is b)  # 比较的是两个变量的内存地址
