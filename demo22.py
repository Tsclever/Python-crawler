# 项目22 异步操作-aiohttp库的使用
# requests.get() 同步的操作 -> 异步操作aiohttp
# pip3 install aiohttp

import asyncio
import aiohttp   # aiohttp是一个强大的异步HTTP客户端和服务器库, 建立在asyncio库至上, 当你定义了一个asyncio异步函数, 可以利用aiohttp来发送异步HTTP请求

urls = [
  "https://i1.huishahe.com/uploads/tu/201910/9999/c52b145ccd.jpg",
  "https://i1.huishahe.com/uploads/allimg/202206/9999/9783c7e78d.jpg",
  "https://i1.huishahe.com/uploads/allimg/202206/9999/b4a96df33b.jpg"
]

# 定义一个协程函数
# 异步下载
async def aiodownload(url, session):
  name = url.rsplit("/", 1)[1]   # 从右边开始分割, 选取右边第一个 / , 索引为 1, 也就是最后一项内容
  # 发送请求, 这里和requests.get()几乎没区别, 除了代理换成了proxy
  async with session.get(url) as resp:   
    # 读取数据, 如果想要源代码, 直接resp.text()即可, 比原来多了个()
    content = await resp.content.read()
    # 写入文件, 有兴趣的话可以尝试一下aiofiles, 一套完整的体系
    with open(name, mode="wb") as file:   
      file.write(content)   # 读取内容是异步的, 需要await挂起
        
  print(name, "搞定")

async def main():
  # 创建session对象 -> 相当于requests对象
  async with aiohttp.ClientSession() as session:
    # 添加下载任务
    tasks = []
    for url in urls:
      tasks.append(aiodownload(url, session))
    # 第二种写法
    # tasks = [aiodownload(url, session) for url in urls]
    
    # 等待所有任务下载完成
    await asyncio.gather(*tasks)

if __name__ == '__main__':
  asyncio.run(main())

