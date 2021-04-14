# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : fucntion_demo.py
# Time       ：2021/4/13 10:14
# Author     ：taoyong
# version    ：python 3.7
"""

# 求出一个数字   个位数和十位数


"""
# 定义
def 方法名（参数）
    方法体
def：方法定义关键字，固定写法
方法名：一个文件中不出现同名的
参数：方法里边的变量有作用域的限制，外部数据必须通过参数传入
方法体:方法逻辑代码
return:可以把return后边

"""

"""
# 方法调用
方法名（实参）

"""


def get_gewei_shiwei(a):
    if a < 10:
        print("个位数为：{}".format(a))
    else:
        ge_wei = a % 10  # 个位数
        a = a // 10
        shi_wei = a % 10
        print("十位数：{}，个位数：{}".format(shi_wei, ge_wei))


get_gewei_shiwei(5)
get_gewei_shiwei(20)
get_gewei_shiwei(100)


# 加关键字可以更改位置，例：host="192.168.3.190"


def coonect_msyql(host, user, pwd, datebase, port="3308", charset="utf-8"):
    print(host, user, pwd, datebase, port, charset)
    print("连接了数据")


# coonect_msyql(host="192.168.3.190", pwd="root", datebase="root", user="sl_stu", charset="3308")

"""
*args: 在参数列表中，相当于把所有的位置参数放到一个args的元组中；方法调用的时候，*相当于拆包，把元组中的数据全部取出，按照顺序传入方法中
**kwargs: 在参数列表中，相当于把所有的关键字参数放到一个kwargs的字典中；** 相当于拆包，把字典中的数据全部取出，按照关键字传参的方式传入方法中

"""


def mysql_tools(*args, **kwargs):
    print(args, kwargs)
    print("开始连接数据库")
    coonect_msyql(*args, **kwargs)
    print("数据库连接成功")


mysql_tools("192.168.3.190", "root", "root", "sl_stu", port="3308")

# 内置方法 （函数）

print(1, 2, end="")  # 输出变量内容到控制台
len("123456789")  # 返回容器中的项目数
range(10)  # 返回一个自增或者自减的序列
set()  # 创建一个空集合，把一个序列转换成一个集合
list()  # 创建一个空列表，把一个序列转换成一个列表
tuple()  # 创建一个空元组，把一个序列转换成一个元组
str()  # 创建一个空字符串，把一个序列转换成一个字符串
int()  # 创建一个数字类型的字符串转换成一个整数
dict()  # 创建字典
id(12)  # 返回变量的地址
isinstance("123", str)  # 判断一个变量是否指定类型
# print(str([1,2,3,4,5]))   # "[1,2,3,4,5]"
print(int("123") + 3)

d1 = {"name": "asd"}
d2 = {"age": "123"}
d = dict(d1, **d2)
print(d)

"""
打开模式：
    普通模式
    w:写入,清空文件内容
    r:读取，打开文件必须是已存在的文件，不然会报错
    a:追加写入，不会清空文件内容
二进制模式（非纯文本文件），
    b:以二进制流的形式打开文件

"""

f = open("aa.txt", "w", encoding="utf-8")  # 打开一个文件
f.write("hello,阿斯顿")  # 写入内容到文件
f.write("hello,阿斯顿\n")  # 写入内容到文件  换行
f.write("hello,阿斯顿\n")  # 写入内容到文件  换行
f.write("hello,阿斯顿")  # 写入内容到文件
f.write("hello,阿斯顿")  # 写入内容到文件
f.close()  # 关闭文件

f = open("aa.txt", "r", encoding="utf-8")  # 打开一个文件
print(f.read())
f.close()


