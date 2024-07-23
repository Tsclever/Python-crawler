# 项目19 线程池和进程池
# 线程池: 一次性开辟一些线程, 我们用户直接给线程池子提交任务, 线程任务的调度交给线程池来完成。   适合 I/O 密集型任务，如网络请求、文件读写、数据库操作等。
# 进程池: 一次性创建多个进程来管理任务调度，用户只需提交任务，具体的进程调度由进程池自动完成。    适合 CPU 密集型任务，如大数据处理、复杂计算等。

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor   # ThreadPoolExecutor线程池, ProcessPoolExecutor进程池

def fn(name):
  for i in range(1000):
    print(name, i)


if __name__ == '__main__':
  # 创建线程池
  with ThreadPoolExecutor(50) as t:   # 创建一个拥有50个线程的线程池
    # 提交 100 个任务到线程池中  
    for i in range(100):   # 每个线程完成任务后, 会继续执行下一个任务, 并会被重新命名, 所以才会出现100个线程名, 但真实的线程才50个
      t.submit(fn, name=f"线程{i}")    # 给线程池分配任务
  
  # 等待线程池中的任务全部执行完毕, 才继续执行(守护)   类似于break
  print("over!")

if __name__ == '__main__':
  # 创建线程池
  with ProcessPoolExecutor(50) as t:   # 创建一个拥有50个线程的线程池
    # 提交 100 个任务到线程池中  
    for i in range(100):   # 每个线程完成任务后, 会继续执行下一个任务, 并会被重新命名, 所以才会出现100个线程名, 但真实的线程才50个
      t.submit(fn, name=f"线程{i}")    # 给线程池分配任务
  
  # 等待线程池中的任务全部执行完毕, 才继续执行(守护)   类似于break
  print("over!")






