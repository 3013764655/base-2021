# # !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_demo.py
# Time       ：2021/4/14 10:08
# Author     ：taoyong
# version    ：python 3.7
"""

"""
class 类名（）
    属性
    方法

class：固定写法，表示创建一个类
类名：类的名字
（）：空着
属性：类变量
方法：魔法方法、实例方法、类方法、静态方法

# 实例化类 => 对象
类名（实参）# 传参参考类中__init__方法的参数，忽略第一个参数

"""

std1 = {'name': 'Michael', 'score': 98}  # 表一 std1  std1内容为 'name': 'Michael', 'score': 98
std2 = {'name': 'Bob', 'score': 81}  # 表二 std2   std2内容为 'name': 'Bob', 'score': 81


def print_score(std):  # 定义 函数名为print_score （实参）为std
    print('%s: %s' % (std['name'], std['score']))  # 字符串格式化   %s:%s =  name:score


print_score(std1)  # 打印结果 std1
print_score(std2)  # 打印结果 std2


# 属性
# 类变量
class Student(object):
    # 定义在类中而不是方法中
    name = None  # 类变量
    score = None  # 类变量

    def print_score(self):
        print("%s:%s" % (self.name, self.score))


# 实例变量
class Student(object):  # 创建类名（student）  实参（object）

    def __init__(self, name, score):  # 定义
        """
        实例变量定义在类的实例方法中
        :param name:
        :param score:
        """
        self.name = name
        self.score = score

    def print_score(self):  # 定义 函数名为print_score （实参）为self
        print('%s: %s' % (self.name, self.score))  # 字符串格式化   %s:%s =  name:score


a = Student("Michael", 98)  # 赋值a = 函数名为student 中的实参 "Michael", 98
a.print_score()
print(a.name)  # 打印结果 name

# 类变量特征
# 1、可以直接通过类名访问
Student.name = "小明"
Student.score = "80"
print(Student.name)
print(Student.score)
# 2、类变量是类的所有实例共享
s1 = Student("小明", "80")
s2 = Student("小红", "40")
s1.print_score()
s2.print_score()

# 实例变量特征
# 1、需要通过对象访问，不能使用类名访问
s1 = Student("小明", "80")
print(s1.name)

# 2、对象之间的实例变量不共享
s2 = Student("小明", "90")
print(s2.name)


# 方法
# 魔法方法
# 1、所有的魔法方法名字，都是python解释器定义好的
# 2、所有的魔法方法都是python解释器在某个特定语法中自动调用
class Student(object):  # 创建类名（student）  实参（object）

    def __init__(self, name, score):  # 定义
        """
        类实例化的时候，会被自动调用
        :param name:
        :param score:
        """
        self.name = name
        self.score = score

    def print_score(self):  # 定义 函数名为print_score （实参）为self
        print('%s: %s' % (self.name, self.score))  # 字符串格式化   %s:%s =  name:score


s1 = Student("校长", "10")
s1.print_score()
del s1


# 类的实例方法
# 特征1、类的普通方法和魔法方法都是实例方法  2、实例方法只能通过对象来调用
class Student(object):  # 创建类名（student）  实参（object）

    def __init__(self, name, score):
        """
        类的实例方法
        :param name:
        :param score:
        """
        self.name = name
        self.score = score

    def print_score(self):
        """
        类的实例方法
        :return:
        """
        print('%s: %s' % (self.name, self.score))


# 类方法
# 1、定义的时候，需要使用@classmtho装饰器  2、类方法可以通过类名直接调用   3、建议类方法中，第一个变量名改成cls
class Student(object):
    # 定义在类中而不是方法中
    name = None  # 类变量
    score = None  # 类变量

    @classmethod
    def print_score(cls):  # cls 代表本身
        print("%s:%s" % (cls.name, cls.score))


Student.print_score()


# 静态方法
# 1、静态方法定义时，需要使用@steatmates装饰器
# 2、没有第一个参数，无法直接访问类内部的其他方法和属性
class Student(object):

    @staticmethod
    def print_score(name, score):
        print("%s:%s" % (name, score))


Student.print_score("小明", "234")


# 面向对象编程  封装  继承  多态

# 封装
# 1、只能通过类名和对象来访问类中定义好的变量和方法
# 2、权限控制，公开私有化
#       公开:可以通过类名或者对象直接访问
#       私有：只能在类内部通过self，cls变量访问，而不能通过类名或者对象直接访问
class Student(object):
    # 定义在类中而不是方法中
    __name = "小明"  # 私有变量
    score = "29"  # 公开的变量

    @classmethod
    def print_score(cls):  # cls 代表本身
        print("%s:%s" % (cls.__name, cls.score))


Student.print_score()


# 继承
class Animal():  # 父类
    def run(self):
        print("Animal is running...")


# 子类
class Dog(Animal):
    pass


# 子类
class Cat(Animal):  # 继承的语法，子类继承父类中所有公开的方法和属性
    pass


d = Dog()
d.run()
c = Cat()
c.run()


# 方法重写
class Animal():  # 父类
    def run(self):
        print("Animal is running...")


# 子类
class Dog(Animal):
    def run(self):
        print("dog is running...")

    def aciton(self):
        super().run()  # super 可以获取父类对象


# 子类
class Cat(Animal):
    def run(self):
        print("cat is running...")


d = Dog()
# d.run()
c = Cat()
c.run()


# c.run()

# 多态
class Animal():  # 父类
    def run(self):
        print("Animal is running...")


# 子类
class Dog(Animal):
    def run(self):
        print("dog is running...")

    def action(self):
        super().run()  # super 可以获取父类对象


# 子类
class Cat(Animal):
    def run(self):
        print("cat is running...")


# 传入继承链中具有相同方法的对象，去调用这个方法。传入的对象不同，调用的方法也不同
def action(obj):
    obj.run()


action(Animal())
action(Dog())
action(Cat())


# 鸭子类型
class Animal():  # 父类
    def run(self):
        print("Animal is running...")


# 子类
class Dog(Animal):
    def run(self):
        print("dog is running...")

    def action(self):
        super().run()  # super 可以获取父类对象


# 子类
class Cat():
    def run(self):
        print("cat is running...")


# 鸭子类型，只是要求对象中具备某个共同的方法，你要求任何的继承关系
def action(obj):
    obj.run()


action(Animal())
action(Dog())
action(Cat())
