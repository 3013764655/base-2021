# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : var_str.py
# Time       ：2021/4/7 10:17
# Author     ：taoyong
# version    ：python 3.7
"""

# 转义符 \n 普通字符加上转义符，表示有特殊含义。特殊字符加上转义符表示就是一个普通字符
s = "汉字abc123_n,.\nsdfasf\"nakhda\tjashdjl"
print(s)
s = 'ahgsdha"jahsjhdga'
# 访问字符串中的字符
s = "12345789vghada"  # 下标从0开始
print(s[3])  # [] 取下标

# 字符串截取 s[n:m]  n表示起始下标，m表示结束下标+1
# 截取下标2-8的字符
print(s[2:9])

# s[n:]  表示从下标为n的字符开始，截取到字符串结尾
print(s[2:])

# s[：m]  表示从下标为0的字符开始，截取到下表为m-1的字符为止
print(s[:9])

# 下标可以为负，倒着数，从-1开始
print(s[-6: -2])

# s[n:m:step] step: 步长，默认为1
print(s[1:11:2])

# s[::step] step: 步长可为负数,从后往前截取
print(s[-2:-10:-1])

# 拼接 两个字符串拼接到一起，但是两个字符串本身不发生变化
s1 = "abc"
s2 = "123"
print(s1 + s2)
print(s1)
print(s2)

# 前后去空格
s = " aaa "
print(s.strip())

# 去除左边空格
print(s.lstrip())

# 去除右边空格
print(s.rstrip())

# 切片  把字符串根据指定字符切割成n个子串，并放入一个列表中
s = "姓名,年龄,性别,住址"
print(s.split(","))

# 替换
'''
str.replace(old.new)
old:表示被替换的字符串
new：表示要替换的字符串
把字符串中的所有的old变量代表的字符串，替换成new变量代表的字符串，
'''
s = "姓名,年龄,性别,住址"
s = s.replace(",", ",")
print(s)

# 查找
'''
str.find(s)
在字符串str中查找s子串，如果查找到返回s子串第一个字符所在的下标，如果查找不到则返回-1
'''
s = "nahsdkuhakhdakjas"
print(s.find("Hello"))  # 可以查找到 返回5
print(s.find("hello111"))  # 查找不到 返回-1

# 格式化
name = "小红"
age = "18"
s = "我叫:" + name + ",今年:" + age + "岁"
print(s)

# 占位符格式化
name = "小红"
age = "18"
s = "我叫:%s,今年:%s岁" % (name, age)
print(s)

# format
name = "小红"
age = "18"
money = 12345.65
s = "我叫:{},今年:{}岁,我有{}元".format(name, age, money)
print(s)
