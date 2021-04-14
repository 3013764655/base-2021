# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : var_live.py
# Time       ：2021/4/14 14:13
# Author     ：taoyong
# version    ：python 3.7
"""
a = 10  # 创建一个变量
# 变量回收
# 主动回收
del a  # 使用del关键字销毁变量


# python 虚拟机自动回收  python 垃圾回收机制
# 模块中定义的变量，程序执行结束才会被回收 全局变量
# 方法中定义的变量，方法执行结束之后就会被回收  局部变量
def aaa():
    b = 10  # 局部变量
    print(b)


aaa()

# 变量作用域

a = 28


def bbb():
    # print(a)  # 访问a变量的值
    global a  # 声明a 变量时全局变量
    a = 20  # 修改a变量的值


bbb()
print(a)
