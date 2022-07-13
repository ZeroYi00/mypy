#!/usr/bin/python3

import threading, time

# 创建锁
thread_lock = threading.Lock()
# 创建线程列表
threads = []


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Thread Start: " + self.name)
        # 获取锁，同步线程
        thread_lock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        thread_lock.release()
        print("Thread Exit: " + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("{}: {}".format(thread_name, time.ctime()))
        counter -= 1


## Lock 和 Rlock
# 使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法
# 对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。
if __name__ == '__main__':
    # 创建线程
    thread1 = myThread(1001, "Thread-1", 1)
    thread2 = myThread(1002, "Thread-2", 2)

    # 开启线程
    thread1.start()
    thread2.start()

    # 添加线程列表
    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程完成 (阻塞)
    for t in threads:
        t.join()
    print("exit")
