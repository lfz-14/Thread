# import threading

import time
import multiprocessing

# 主进程，子进程
# 进程占用的资源较大，线程占用的资源少
# 进程数不是越多越好，根据电脑的资源来分配
# 写时拷贝  多线程应用更多
# 现有进程，再有线程
def test1():
    while True:
        print("1-----")
        time.sleep(1)


def test2():
    while True:
        print("2-----")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
