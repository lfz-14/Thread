import time
import threading
# 时间片轮转
# 并行：真的多任务   只能在多核CPU上实现
# 并发：假的多任务
# 线程的创建谁先执行不确定  可以通过延时方法
# 主线程不能在子线程之前结束
def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print("----正在唱：ready go!----")
        time.sleep(1)


def dance():
    """跳舞5秒钟"""
    for i in range(5):
        print("----正在跳舞----")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()