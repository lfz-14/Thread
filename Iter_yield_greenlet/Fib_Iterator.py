class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    # 添加实例方法 iter
    def __iter__(self):
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用for,那么必须实现__iter__方法"""
        return self  # 返回值是一个包含__iter__和__next__方法的对象方法的引用  这个对象称为迭代器

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fibonacci(10)

for num in fibo:
    print(num)

