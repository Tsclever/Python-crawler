# 项目25 先来个简单的视频网站练练手(爬取看剧啦网站)
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


# 1.拿到85576-1-1.html的页面源代码
url = "https://www.kanju7.com/play/85576-1-1.html"
headers = {
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
# print(resp.text)


# 2.从源代码中提取到m3u8的url
obj = re.compile(r'<div class="info clearfix">.*?"url":"(?P<url>.*?)",', re.S)   # 用来提取m3u8的地址
m3u8_url = obj.search(resp.text).group("url").replace("\\", "")   # 拿到m3u8地址
# print(m3u8_url)

# 获取链接的后半段部分
resp2 = requests.get(m3u8_url, headers=headers)
obj2 = re.compile(r'#EXT-X-STREAM-INF.*?\n(?P<url2>.*?)\n', re.S)   # 一共是三段内容, 最后一段是在第三行, 所以 匹配到换行符<分组>再匹配到换行符 .*?\n(?P<url2>.*?)\n
m3u8_url2 = obj2.search(resp2.text).group("url2")
# print(m3u8_url2)

# 拼接成完整的链接52
# m3u8_url3 = m3u8_url.replace("index.m3u8", m3u8_url2)   # 方法行不通
# m3u8_url3 = m3u8_url.rsplit("/", 1)[0] + "/" + m3u8_url2   # 方法行不通
path = m3u8_url.rsplit("/", 1)[0] + "/"
m3u8_url3 = urljoin(path, m3u8_url2)   # urljoin()方法, 拼接字符串
# print(path)

# 3.下载m3u8文件
resp3 = requests.get(m3u8_url3, headers=headers)
# print(resp3.text)
obj3 = re.compile(r'<span class="text-muted">.*?</span>.*?>(?P<name>.*?)</a>')

name = obj3.search(resp.text).group("name")
# print(name)

with open(f"{name}.m3u8", mode="wb") as f:
  f.write(resp3.content)


# 4.解析m3u8文件
n = 1   # 计数

with open(f"{name}.m3u8", mode="r", encoding="utf-8") as f2:
  for line in f2:
    line = line.strip()   # 去掉空格, 空白, 换行符
    if line.startswith("#"):   # 如果以 # 开头, 我不要
      continue
    # print(line)

    # 下载视频片段
    resp4 = requests.get(line)
    with open(f"video/{n}.ts", mode="wb") as f3:
      f3.write(resp4.content)
    
    print(f"{n}.ts over!")
    n += 1 


# 5.合并视频
# 这里就需要依靠外部的软件来进行视频合成了