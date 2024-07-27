# 项目23 扒光一本小说(异步下载)

# 小说简介链接, 只需要请求一次, 所以不需要异步
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# 小说第一章链接, 这里就需要异步操作, 同时下载
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

"""
1.同步操作: 访问getCatalog, 拿到所有章节cid和名称
2.异步操作: 访问getChapterContent, 下载所有的章节内容
"""

import requests
import asyncio
import aiohttp
import aiofiles
import json
import os

async def aiodownload(cid, b_id, title):
  data = {
    "book_id":b_id,
    "cid":f"{b_id}|{cid}",
    "need_bookinfo":1
  }
  data = json.dumps(data)   # data是个字典, 需要用json.dumps转换成json格式
  url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

  async with aiohttp.ClientSession() as session:   # 构建异步http对象
    async with session.get(url) as resp:   # 构建异步请求
      json_data = await resp.json()   # 由于是异步函数, 所以需要用await挂起

      # 创建目录
      name = "西游记"
      directory = os.path.join(f"/mnt/e/work/download/{name}") # directory = os.path.join("/mnt/e/work/download/", name)两个代码效果一样, 都是把地址连起来
      os.makedirs(directory, exist_ok=True)   # 确保目录存在, 如果不存在则创建, 有个误区, directory里存的是地址, 真正创建的代码是os.makerirs
      file_path = os.path.join(directory, title + ".txt")

      async with aiofiles.open(file_path, mode="w", encoding="utf-8") as f:
        await f.write(json_data['data']['novel']['content'])   # 把小说内容写出
        
        # json_data['data']['novel']['content']   # 文章内容

      # 第二种方法
      # dic = await resp.json()

      print(f"{title}over!")

async def getCatalog(url):
  resp = requests.get(url)
  json_data = json.loads(resp.text)
  tasks = []
  contents = json_data['data']['novel']['items']   # items就是对应每一个在章节的名称和cid
  # print("b_id:",b_id)
  for items in contents:
    title = items['title']
    cid = items['cid']
    # 准备异步任务
    tasks.append(aiodownload(cid, b_id, title))   # aiodownload(cid, b_id, title) 这个函数调用会被执行, aiodownload函数的返回值会被添加到tasks列表中
    # print(cid, title)
  
  # 等待所有任务下载完成
  await asyncio.gather(*tasks)   # 当所有任务都完成时，asyncio.gather(*tasks) 将返回一个包含每个任务结果的列表，这些结果按照任务在 tasks 列表中出现的顺序排列。

  # 第二种写法
  # dic = resp.json()   # 转换为字典
  # for items in dic['data']['novel']['items']:   
  

if __name__ == '__main__':
  b_id = "4306063500"
  url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
  asyncio.run(getCatalog(url))   # 先传参, 再执行函数
