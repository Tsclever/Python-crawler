# 项目21 协程的概念

# input() 程序也是处于阻塞状态
# requests.get(bilibili) 在网络请求返回数据之前, 程序也是处于阻塞状态
# 一般情况下, 当程序处于 IO 操作的时候, 线程都会处于阻塞状态

# 协程: 当程序遇见了 IO 操作的时候, 可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换, 切换条件一般就是 IO 操作
# 在宏观上, 我峨嵋你能卡电脑的其实是多个任务一起在执行
# 多任务异步操作

# 上方所讲的一切, 都是在单线程的条件下
# 单线程异步

import time
import asyncio   # 是一个用于编写单线程并发代码的库, 它提供了编写异步程序的基础设施

# def func():
#   print("我爱黎明")
#   time.sleep(3)   # 让当前的线程处于阻塞状态, cpu是不为我工作的
#   print("我真的爱黎明")

# if __name__ == '__main__':
#   func()


# async def func():
#   print("你好啊, 我叫赛利亚")

# if __name__ == "__main__":
#   g = func()   # <coroutine object func at 0x7f954d402500> func是一个协程对象
#   # print(g)   
#   asyncio.run(g)   # 协程程序运行需要asyncio模块的支持


# 同步操作(程序结束后再执行下一个程序)
# async def func1():
#   print("你好啊, 我叫1号")
#   time.sleep(3)   # 当程序出现了同步操作的时候, 异步就中断了
#   print("你好啊, 我叫1号")

# async def func2():
#   print("你好啊, 我叫22号")
#   time.sleep(2)
#   print("你好啊, 我叫22号")

# async def func3():
#   print("你好啊, 我叫333号")
#   time.sleep(4)
#   print("你好啊, 我叫333号")

# if __name__ == '__main__':
#   f1 = func1()
#   f2 = func2()
#   f3 = func3()
#   lists = [
#     f1, f2, f3
#   ]

#   t1 = time.time()

#   # 一次行启动多个任务(协程)
#   asyncio.run(asyncio.wait(lists))   # 多个任务需要交给asyncio.wait处理

#   t2 = time.time()
#   print(t2 - t1)   总需9秒


# 异步操作(程序结束后再执行下一个程序)
# async def func4():
#   print("你好啊, 我叫1号")
#   # time.sleep(3)   # 当程序出现了同步操作的时候, 异步就中断了
#   await asyncio.sleep(3)   # 异步操作   await 可以理解为程序挂起, 3个await一起干
#   print("你好啊, 我叫1号")

# async def func5():
#   print("你好啊, 我叫22号")
#   await asyncio.sleep(2)
#   print("你好啊, 我叫22号")

# async def func6():
#   print("你好啊, 我叫333号")
#   await asyncio.sleep(4)
#   print("你好啊, 我叫333号")

# if __name__ == '__main__':
#   f4 = func4()
#   f5 = func5()
#   f6 = func6()
#   lists = [
#     f4, f5, f6
#   ]

#   t1 = time.time()

#   # 一次行启动多个任务(协程)
#   asyncio.run(asyncio.wait(lists))   # 多个任务需要交给asyncio.wait处理

#   t2 = time.time()
#   print(t2 - t1)   # 总需4秒


# async def func1():
#   print("你好啊, 我叫1号")
#   await asyncio.sleep(3)   # 异步操作   await 可以理解为程序挂起, 3个await一起干
#   print("你好啊, 我叫1号")

# async def func2():
#   print("你好啊, 我叫22号")
#   await asyncio.sleep(2)
#   print("你好啊, 我叫22号")

# async def func3():
#   print("你好啊, 我叫333号")
#   await asyncio.sleep(4)
#   print("你好啊, 我叫333号")

# async def main():   # await 必须写在async协程函数里
#   # 第一种写法
#   # f1 = func1()
#   # await f1   # 一般await挂起操作放在协程对象前面

#   # 第二种写法
#   tasks = [
#     func1(), func2(), func3()
#   ]
#   # await asyncio.wait(tasks)   # The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
#                                 # 从 Python 3.8 开始，直接传递协程对象（coroutine objects）到 asyncio.wait() 已经被弃用，并在未来的 Python 3.11 版本中计划移除这一功能。
#   await asyncio.gather(*tasks)  # 建议使用 asyncio.gather 方法, 注意 *tasks 的使用，它解包了列表 tasks，将里面的协程对象作为单独的参数传递给 asyncio.gather()。                      

# if __name__ == '__main__':
#   t1 = time.time()
#   # 一次行启动多个任务(协程)
#   asyncio.run(main())
#   t2 = time.time()
#   print(t2 - t1)   
  

# 伪代码(模板)
# 在爬虫领域的应用
async def download(url):
  print("开始下载")
  await asyncio.sleep(2)   # 模拟网络请求   requests.get()
  print("下在完成")

async def main():
  urls = [
    "http://baidu.com",
    "http://bilibili.com",
    "http://sogou.com"
  ]

  tasks = []
  for url in urls:
    d = download(url)
    tasks.append(d)

  # await asyncio.wait(tasks)
  await asyncio.gather(*tasks)

if __name__ == '__main__':
  asyncio.run(main())