# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : var_dict.py
# Time       ：2021/4/7 15:47
# Author     ：taoyong
# version    ：python 3.7
"""
# 新建字典
# 空字典
d = {}
print(d)

d = dict()
print(d)

# 新建有数据的字典
d = {"name": "小明", "age": 18}
print(d)
d = dict(name="小明", age=18)
print(d)

# 修改字典元素的值
d = {"name": "小明", "age": 18}
d["age"] = 20
print(d)

# 根据key访问value
d = {"name": "小明", "age": 18}
print(d["name"])

# 新增一对数据
d = {"name": "小明", "age": 18}
d["sex"] = "男"
print(d)

# 新增多对数据

# 更新原字典
d = {"name": "小明", "age": 18}
d.update({"sex": "男", "eduction": "大专"})  # 更新旧字典，把新字典中的数据更新到旧字典中
print(d)

# 合并两个字典
d1 = {"name": "小明", "age": 18}
d2 = {"sex": "男", "eduction": "大专"}
# print(dict(d1,"sex": "男", "eduction": "大专")) # 把两个字典，合并到一个新字典中，原来的两个字典不发生变化
# 上下两行代码等价
print(dict(d1, **d2))  # 把两个字典，合并到一个新字典中,原来的两个字典不发生变化
print(d1)
print(d2)

# 删除字典中的数据
d = {"name": "小明", "sex": "男", "age": 18}
d.pop("sex")  # 根据key删除字典中的数据
print(d)

# 清空字典
d = {"name": "小明", "sex": "男", "age": 18}
d.clear()  # 清空字典
print(d)
