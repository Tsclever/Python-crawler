# 项目18 多线程
# 项目介绍: 线程, 进程
#          进程是资源单位, 每一个进程至少要有一个线程
#          线程是执行单位

# 启动每一个程序默认都会有一个主线程
from threading import Thread   # 线程类模块


# def func():
#   for i in range(1000):
#     print("func", i)


# if __name__ == '__main__':
#   func()
#   for i in range(1000):
#     print("main", i)


# 多线程

# 方法一
# 小脚本写法

# def func():
#   for i in range(1000):
#     print("支路线", i)

# if __name__ == "__main__":
#   t = Thread(target=func)   # 创建线程并给线程安排任务
#   t.start()   # 开始执行该线程, 多线程状况为可以开始工作状态, 具体的执行时间由cpu决定
#   for i in range(1000):
#     print("我是主路线", i)


# 方法二
# 大佬爱使用
class MyThread(Thread):   # 继承了Thread就是子类, Thread的特性是线程, 那么子类也会有线程的特性
  def run(self):   # 固定的  ->  当线程被执行的时候, 被执行的就是run()
    for i in range(100):
      print("子线程", i)

if __name__ == "__main__":
  t = MyThread()
  # t.run()   # 方法的调用  ->  单线程?
  t.start()   # 开启线程

  for i in range(100):
    print("主路线", i)


