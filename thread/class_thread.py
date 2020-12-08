import threading
import time


# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = "I'm" + self.name + '@' + str(i)
#             print(msg)


class MyThread(threading.Thread):
    def run(self):   # 继承的thread 的方法，通过t.start()自动调用
        self.login()
        self.register()
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + self.name + '@' + str(i)
            print(msg)

    def login(self):
        print("这是 登录.....")

    def register(self):
        print("这是注册的代码.....")

if __name__ == "__main__":
    t = MyThread()
    t.start()
    # t.login()  属于单任务，调用类的方法  不属于多任务


