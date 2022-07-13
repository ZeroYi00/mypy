# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @FileName  :study-queue.py
# @Desc      :线程优先级队列
# @Time      :2022/7/13 22:45
# @Email     :ib_yeang@163.com
# @Author    :Zero Yi

import queue, threading, time

exitFlag = 0
# 创建锁
queueLock = threading.Lock()
# 创建队列
workQueue = queue.Queue(10)


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Thread Start: " + self.name)
        process_data(self.name, self.q)
        print("Thread Exit: " + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("{} processing {}".format(threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


# Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO队列Queue，LIFO队列LifoQueue，和优先级队列 PriorityQueue。

# 这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
# Queue 模块中的常用方法:
# Queue.qsize() 返回队列的大小
# Queue.empty() 如果队列为空，返回True,反之False
# Queue.full() 如果队列满了，返回True,反之False
# Queue.full 与 maxsize 大小对应
# Queue.get([block[, timeout]])获取队列，timeout等待时间
# Queue.get_nowait() 相当Queue.get(False)
# Queue.put(item) 写入队列，timeout等待时间
# Queue.put_nowait(item) 相当Queue.put(item, False)
# Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
# Queue.join() 实际上意味着等到队列为空，再执行别的操作

# 源码中其实实现了三个进程读取同一个队列，按照先进先出原则实现锁定。

# 用start方法来启动线程，真正实现了多线程运行，这时无需等待run方法体代码执行完毕而直接继续执行下面的代码。
# 通过调用Thread类的start()方法来启动一个线程，这时此线程处于就绪（可运行）状态，并没有运行，
# 一旦得到cpu时间片，就开始执行run()方法，这里方法 run()称为线程体，它包含了要执行的这个线程的内容，Run方法运行结束，此线程随即终止。

# join的作用是保证当前线程执行完成后，再执行其它线程。join可以有timeout参数，表示阻塞其它线程timeout秒后，不再阻塞。
# 一般线程的start()之后，所有操作结束后都要进行thread.join()。确保语句的输出是join()后面的程序是等线程结束后再执行的。
if __name__ == '__main__':
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five"]
    threads = []
    threadID = 1

    # 创建新线程
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    # 填充队列
    queueLock.acquire()
    print("队列填充中>>>>>>>>>>>>>>")
    time.sleep(1)
    for word in nameList:
        workQueue.put(word)
    print("队列填充完毕>>>>>>>>>>>>>>")
    queueLock.release()

    # 等待队列清空
    while not workQueue.empty():
        pass

    # 通知线程退出
    exitFlag = 1

    # 等待所有线程完成
    for t in threads:
        t.join()
    print("exit")
