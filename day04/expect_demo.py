# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : expect_demo.py
# Time       ：2021/4/13 16:57
# Author     ：taoyong
# version    ：python 3.7
"""

# # 语法错误:变量先定义，后使用
# print(a)

# 语法没问题，但是程序运行的过程中出问题
# 如果try后边的代码块，运行出错，就会运行except代码块中的代码。否则不会运行except代码块中的代码
try:
    print(6 / 2)
except:
    print("代码执行出问题了")

# except：try代码抛异常，会执行
# else:try代码执行不会出现问题，会执行
# funally: 无论try后边的代码执行是否出现问题，都会执行

try:
    print(1 / 3)
    # open("ssss.txt")
except ZeroDivisionError:
    print("被除数不能为0")
else:
    print("代码没问题")
finally:
    print("代码结束")
