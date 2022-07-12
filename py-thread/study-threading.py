#!/usr/bin/python3
import threading, time


# 创建进程类
class myThread(threading.Thread):
    # 构造函数
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    # 重写run()
    def run(self):
        print("Thread Start：" + self.name)
        print_time(self.name, self.counter, 5)
        print("Thread Exit：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{}: {}".format(threadName, time.ctime(time.time())))
        counter -= 1


## 类封装式
# threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# 线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
#
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
# is_alive(): 返回线程是否活动的
# getName(): 返回线程名
# setName(): 设置线程名
if __name__ == '__main__':
    # 创建线程
    thread1 = myThread(1001, "Thread-1", 1)
    thread2 = myThread(1002, "Thread-2", 2)

    # 开启线程
    print("Thread-1 is Alive? ", thread1.is_alive())
    thread1.start()
    thread2.start()
    print("Thread-1 is Alive? ", thread1.is_alive())
    thread1.join()
    thread2.join()
    print("Thread-1 is Alive? ", thread1.is_alive())
    print("exit")
