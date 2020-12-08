import threading
import time

# 线程共享全局变量
# 定义一个全部变量
g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1

    print("-----in test1 g_num= %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("-----in test2 g_num= %d" % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(10000000000,))   # 创建一个threading实例对象
    t2 = threading.Thread(target=test2, args=(10000000000,))

    t1.start()
    # time.sleep(1)

    t2.start()
    # time.sleep(1)

    # 等待上面的2个线程执行完毕....
    time.sleep(2)
    print("----- in  main  Thread g_num = %d" % g_num)


if __name__ == '__main__':
    main()
