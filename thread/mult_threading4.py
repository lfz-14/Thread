



# #########查看线程从何处开始执行###########

# 当调用Thread的时候，不会创建 线程
# 当调用Thread创建出来的实例对象的start方法地时候才会创建线程以及让这个线程开始运行

import threading
import time


def test1():
    for i in range(5):
        print("-----test1---%d---" % i)
        time.sleep(1)

    # 如果创建Thread时执行的函数，运行结束那么意味着  这个子线程结束了...

def main():
    # 在调用Thread之前先打印当前线程对象
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)  # 仅仅是创建一个对象而已

    # 在调用Thread之后打印
    print(threading.enumerate())

    t1.start()  # 主线程从此处开始执行  线程的执行从start开始

    # 在调用start之后打印
    print(threading.enumerate())
# 默认主线程最后结束
if __name__ == "__main__":
    main()
