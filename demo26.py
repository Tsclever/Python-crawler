# 项目25 爬取看剧啦网站(高速版)
# 网站: 看剧啦
# 地址: https://www.kanju7.com/

"""
流程:
    1.拿到85576-1-1.html的页面源代码
    2.从源代码中提取到m3u8的url
    3.下载m3u8
    4.读取m3u8文件,下载视频
    5.合并视频
"""

import requests
import re
from urllib.parse import urljoin  
import asyncio
import aiohttp
import aiofiles
import os


# 1.拿到页面源代码,提取到m3u8的url
async def seach_m3u8_url(url, headers):
  # 请求到第一个m3u8地址
  async with aiohttp.ClientSession() as session:
    async with session.get(url, headers=headers) as resp1:
      text1 = await resp1.text()   # 挂起页面文本, 同时运行 
      obj1 = re.compile(r'<div class="info clearfix">.*?"url":"(?P<url>.*?)",', re.S)
      m3u8_url = obj1.search(text1).group("url").replace("\\", "")

      # 电影名称
      obj = re.compile(r'<span class="text-muted">.*?</span>.*?>(?P<name>.*?)</a>')
      name = obj.search(text1).group("name")
      print(name)

    # 请求m3u8中视频id
    async with session.get(m3u8_url, headers=headers) as resp2:
      text2 = await resp2.text()   # 挂起页面文本, 同时运行
      obj2 = re.compile(r'#EXT-X-STREAM-INF.*?\n(?P<id>.*?)\n')
      m3u8_url_id = obj2.search(text2).group("id")

      # 拼接m3u8地址和id
      m3u8_url_new = urljoin(m3u8_url.rsplit("/", 1)[0] + "/" , m3u8_url_id)
      async with session.get(m3u8_url_new, headers=headers) as resp3:
        text3 = await resp3.text()   # 挂起页面文本, 同时运行

        # 拿到m3u8的下载地址
        urls = []
        for i in text3.splitlines():   # 用于将字符串 text3 中内容分割成一个列表，其中每个元素都是原字符串中的一行
          if not i.startswith("#"):   # 剔除#开头
            urls.append(i)

  # print(urls)
  return urls,name

# 2.下载m3u8文件
async def m3u8_download(urls, headers, name):
  n = 1   # 计数
  
  # 创建目录
  dir_name = name
  directory = os.path.join("/mnt/e/work/download/", dir_name)
  os.makedirs(directory, exist_ok=True)


  # 开始下载m3u8文件
  async with aiohttp.ClientSession() as session:
    for url in urls:      
      file_path = os.path.join(directory, f"{n}.ts")   # ts文件创建
      async with session.get(url, headers=headers) as resp4:
        async with aiofiles.open(file_path, mode="wb") as f:
          await f.write(await resp4.read())

      print(f"{n}.ts over!")
      n += 1
  print("over")

# 主函数
async def main(url, headers):
  urls, name = await seach_m3u8_url(url, headers)   # seach_m3u8_url()返回的值存入到urls中
  await m3u8_download(urls, headers, name)

# 执行脚本
if __name__ == "__main__":
  url = "https://www.kanju7.com/play/85576-1-1.html"
  headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
  }
  asyncio.run(main(url, headers))


# 3.合并视频
# 这里就需要依靠外部的软件来进行视频合成了