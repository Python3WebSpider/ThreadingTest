import threading, time


def func():
    # 开始处理数据
    global n
    a = n + 1
    time.sleep(0.0001)
    n = a
    # 结束处理


if __name__ == '__main__':
    n = 0
    li = []
    for i in range(1000):
        t = threading.Thread(target=func, args=())
        li.append(t)
        t.start()
    for i in li:
        i.join()  # 等待子线程全部执行完
    print(n)  # 253
