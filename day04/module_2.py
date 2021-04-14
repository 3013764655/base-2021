# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : module_2.py
# Time       ：2021/4/13 14:57
# Author     ：taoyong
# version    ：python 3.7
"""
from day04.module_1 import div

print(div(12, 6))

# 内建模块


import random

print(random.randint(10, 30))  # 获取10到30之间的随机数
print(random.choice([1, 2, 3, 4, 5, 6]))  # 随机获取迭代对象中的一个数据
print(random.choices([1, 2, 3, 4, 5, 6], k=20))  # 随机从指定序列中获取n次数据
print("".join(random.choices("agsjgda", k=8)))

import json

d = """
{"name":"雄安",
"age":20
}
"""
a = json.loads(d)  # 把一个json字符串转换成字典格式
print(a["age"])
# 把一个字典转换成json字符串，ensure_ascii=False :表示不使用ascii码，解决中文乱码问题。indent=2 格式化jaon字符串
print(json.dumps(a, ensure_ascii=False, indent=2))

import os

print(os.path.abspath("aa.txt"))  # 获取文件绝对路径
p = "E:\\workspace\\python\\base-2021\\day04\\aa.txt"
print(os.path.basename(p))  # 获取路径中，最后一个文件或者文件的名字
print(os.path.dirname(p))  # 获取路径中文件夹的路径
print(os.path.isfile(p))  # 判断给定的路径是否存在，并且是一个文件
p = "E:\\workspace\\python\\base-2021\\day04"
print(os.path.isdir(p))  # 判断给定的路径是否存在，并且是一个文件夹
os.system("java")  # 执行cmd命令
