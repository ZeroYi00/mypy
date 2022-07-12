#!/usr/bin/python3

import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

## 函数式
# _thread模块 提供了低级别的、原始的线程以及一个简单的锁
# _thread.start_new_thread ( function, args[, kwargs] )
# 参数说明:
# function - 线程函数
# args - 传递给线程函数的参数,它必须是个tuple类型
# kwargs - 可选参数

if __name__ == '__main__':
    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2,))
        _thread.start_new_thread(print_time, ("Thread-2", 4,))
    except:
        print("Error: 无法启动线程")

    while 1:
        pass
