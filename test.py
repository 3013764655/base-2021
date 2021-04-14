# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test.py
# Time       ：2021/4/6 16:22
# Author     ：taoyong
# version    ：python 3.7
"""
print(1 + 9)
print(9 * 3)
print(3 ** 2)

a = 1 + 9
print(a + 9)

# # 变量重新赋值
a = 5

print(a + 9)

# type() 显示类型
print(type(4))
print(type(6))

a = "123"
print(type("123"))
print(type(a))

# 字符串 引号引起来的
s = "松林学院"
print(type(s))
s = '松林学院'
print(type(s))
s = """
    Hello
    松林学院
    """
print(type(s))
s = '''松林学院
    你好
    '''
print(type(s))

# 数字
# 整数 int
a = 10
print(type(a))

# 浮点数(小数) float
a = 1.1
print(type(a))

# 布尔类型 bool
b = True
print(type(b))
b = False
print(type(b))

# 空类型
n = None
print(type(n))

# 复数类型 conplex
c = complex(3, 4)  # 3 + 4i
print(type(c))

# 列表类型 list
l = [1, "2", True, None, [1, 2, 3], (1, 2, 3), {"name": "松林学院"}]
print(type(l))

# 元组类型  Tuple
t = (1, "2", True, None, [1, 2, 3], (1, 2, 3), {"name": "松林学院"})
print(type(t))

# 集合类型 set
s = {1, 2, True, None}
print(type(s))

# 字典类型 dict
d = {
    "number": 1,
    "str": "123",
    "bool": True,
    "None": None,
    "list": [1, 2, 3, 4],
    "Tuple": (1, 2, 3, 4),
    "set": {1, 2, 3, 1}
}
print(type(d))
