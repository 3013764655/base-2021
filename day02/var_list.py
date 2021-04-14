# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : var_list.py
# Time       ：2021/4/7 14:01
# Author     ：taoyong
# version    ：python 3.7
"""
l = [1, 2, 3, 4, 5, 6, "a", "v", "c", "b"]

# 访问列表中的指定元素
print(l[3])  # [] 取下标

# 列表截取 l[n:m]  n表示起始下标，m表示结束下标+1
# 截取下标2-8的字符
print(l[2:9])

# l[n:]  表示从下标为n的字符开始，截取到列表结尾
print(l[2:])

# l[：m]  表示从下标为0的字符开始，截取到下表为m-1的字符为止
print(l[:9])

# 下标可以为负，倒着数，从-1开始
print(l[-6: -2])

# l[n:m:step] step: 步长，默认为1
print(l[1:11:2])

# l[::step] step: 步长可为负数,从后往前截取
print(l[-2:-10:-1])

# 拼接 两个列表拼接到一起，但是两个列表本身不发生变化
l1 = "abc"
l2 = "123"
print(l1 + l2)
print(l1)
print(l2)

# 修改指定下标的数据
l = [1, 2, 3, 4, 5, 6, 7, 8]
l[2] = 10
print(l)

# 修改列表连续的一段内容
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:4] = 10, 20
print(l)

# 新增数据

# 列表末尾添加单个数据
l = [1, 2, 3, 4]
l.append(10)
print(l)

# 列表末尾添加多个数据
# extend 跟可迭代对象,字符串，列表，元组，集合，字典
# 字符串
l = [1, 2, 3, 4, 5, 6]
l.extend("gha")
print(l)
# 列表
l = [1, 2, 3, 4]
l.extend([6, 7, 8, 9])
print(l)

# 元组
l = [1, 2, 3, 4]
l.extend((6, 7, 8, 9))
print(l)

# 集合
l = [1, 2, 3, 4]
l.extend({6, 7, 8, 9})
print(l)

# 字典
l = [1, 2, 3, 4]
l.extend({"name": "小明", "age": 18})
print(l)

# 通过下标插入数据，插入单个数据
l = [1, 2, 3, 4, 5]
l.insert(1, 10)
print(l)

# 通过下标插入数据，插入多个数据
l = [1, 2, 3, 4, 5]
l[1:1] = [10, 20]
print(l)

# 删除数据
l = [1, 2, 3, 4, 5]
l.remove(2)  # 只会删除第一个匹配到的元素
print(l)

# 删除列表最后一个元素
l = [1, 2, 3, 4, 5, 6]
l.pop()
print(l)

# 删除列表指定下标的元素
l = [1, 2, 3, 4, 5, 6]
l.pop(2)
print(l)

# 查询元素下标
l = [1, 2, 3, 4, 5, 6]
print(l.index(4))  # 列表中存在，返回下标
# print(l.index(7))  # 列表中不存在，抛异常

# 排序
# 升序
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
l.sort()  # 默认升序
print(l)

# 降序
l = [2, 46, 8, 2, 75, 7, 51, 8, 4, 7, 58]
l.sort(reverse=True)  # reverse=True 表示降序排序
print(l)
