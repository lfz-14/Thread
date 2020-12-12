# 函数名():调用函数
# 函数名: 告诉函数在哪儿
# 主线程结束，子线程也结束 整个线程结束
# 主线程等子线程结束之后再结束

# #########查看线程数量###########
import threading
import time


def test1():
    for i in range(5):
        print("-----test1---%d---" % i)


def test2():
    for i in range(5):
        print("-----test2---%d---" % i)


def main():
    t1 = threading.Thread(target=test1)  # 仅仅是创建一个对象而已  做准备工作    t1指向一个实例对象
    t2 = threading.Thread(target=test2)

    t1.start()  # 主线程从此处开始执行

    time.sleep(1)
    print("----1----")

    t2.start()

    time.sleep(1)
    print("----2----")

    print(threading.enumerate()) # TODO


if __name__ == "__main__":
    main()
