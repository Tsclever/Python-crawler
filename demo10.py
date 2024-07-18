# 项目10 爬取优美图库
# 项目介绍: 1.拿到主页面的源代码, 然后提取到子也买呢的链接地址, href
#          2.通过href拿到子页面的内容, 从子页面中找到图片的下载地址  img -> src
#          3.下载图片

import requests
from bs4 import BeautifulSoup
import time   # Python 自带的标准库中包含了 time 模块

url = "http://www.umeituku.com/weimeitupian/"

resp = requests.get(url)
resp.encoding="utf-8"   # 处理乱码
# print(resp.text)

# 把源代码存到BeautifulSoup
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", {"class":"TypeList"}).find_all("a")
# print(alist)

for a in alist:
  href = a.get("href")   # 直接通过get就可以拿到属性的值

  # 拿到子页面的源代码
  chid_resp = requests.get(href)
  chid_resp.encoding = "utf-8"

  # 从子页面中拿到图片的下载路径
  chid_page = BeautifulSoup(chid_resp.text, "html.parser")
  p = chid_page.find("p", align="center")
  img = p.find("img")
  src = img.get("src")   # 这里需要注意一下, .get 不能直接再bs对象上操作

  # 下载图片
  img_resp = requests.get(src)    # 先发送请求, 再切割链接作为名字, 这里容易搞混
  img_name = src.split("/")[-1]   # 通过 "/" 来切割, 并且取到最后一个内容
  with open("img/"+img_name, "wb") as file:   # 先用切割好的名字创建文件
    # img_resp.content   # 这里拿到的是字节       
    file.write(img_resp.content)              # 再用从请求中获得的二进制写入到文件中, 这里也容易搞混

  print("over!", img_name)
  time.sleep(1) # 设置1秒延迟

print("完成！")

