import threading
import time


# 线程共享全局变量
# 定义一个全部变量

def test1(temp):
    temp.append(33)

    print("-----in test1 g_num= %s" % str(temp))


def test2(temp):
    print("-----in test2 g_num= %s" % str(temp))


g_nums = [11, 22]


def main():
    # target 指定将来 这个线程去哪个函数执行代码
    # args 指定将来调用 函数的时候 传递什么数据过去
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)
    print("----- in  main  Thread g_num = %s" % str(g_nums))


if __name__ == '__main__':
    main()
