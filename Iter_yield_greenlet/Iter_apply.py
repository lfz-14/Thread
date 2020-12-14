# from collections import Iterable
#
# isinstance(100, Iterable)  # 判断对象是否是可迭代的
#
# # 只定义普通的类和迭代器没有太大关系
# class Classmate(object):
#     def __init__(self):
#         self.names = list()
#
#     def add(self, name):
#         self.names.append(name)
#
#
#
# classmate = Classmate()  # classmate:类创建出来的实例对象
#
# classmate.add("老王")
# classmate.add("王二")
# classmate.add("张三")
#
#
# for name in classmate:
#     print(name)
'''运行结果:
Traceback (most recent call last):
  File "E:/study/python/threading_mult/Iter_yield_greenlet/Iter_apply.py", line 21, in <module>
    for name in classmate:
TypeError: 'Classmate' object is not iterable'''

# from collections import Iterable
#
# isinstance(100, Iterable)  # 判断对象是否是可迭代的
#
#
# # 只定义普通的类和迭代器没有太大关系
# class Classmate(object):
#     def __init__(self):
#         self.names = list()
#
#     def add(self, name):
#         self.names.append(name)
#
#     # 添加实例方法 iter
#     def __iter__(self):
#         """如果想要一个对象称为一个 可以迭代的对象，即可以使用for,那么必须实现__iter__方法"""
#         pass
#
#
# classmate = Classmate()  # classmate:类创建出来的实例对象
#
# classmate.add("老王")
# classmate.add("王二")
# classmate.add("张三")
#
# print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))  # True
#
# for name in classmate:
#     print(name)

"""运营结果
DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
  from collections import Iterable
Traceback (most recent call last):
  File "E:/study/python/threading_mult/Iter_yield_greenlet/Iter_apply.py", line 24, in <module>
    for name in classmate:
TypeError: iter() returned non-iterator of type 'NoneType'"""

from collections.abc import Iterable, Iterator

import time
# isinstance(100, Iterable)  # 判断对象是否是可迭代的


# 只定义普通的类和迭代器没有太大关系
class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    # 添加实例方法 iter
    def __iter__(self):
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用for,那么必须实现__iter__方法"""
        return ClassIterator()  # 返回值是一个包含__iter__和__next__方法的对象方法的引用  这个对象称为迭代器


class ClassIterator(object):  # 迭代器：包含__iter__和__next__方法
    def __iter__(self):
        pass

    def __next__(self):  # 用来记录
        return 11


classmate = Classmate()  # classmate:类创建出来的实例对象

classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))  # True
#
# classmate_iterator = iter(classmate)  # 自动调用iter方法
# print("判断classmate是否是迭代器：", isinstance(classmate_iterator, Iterator))
#
# print(next(classmate_iterator))
for name in classmate:
    print(name)
    time.sleep(1)
