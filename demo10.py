# 项目10 爬取优美图库
# 项目介绍: 1.拿到主页面的源代码, 然后提取到子也买呢的链接地址, href
#          2.通过href拿到子页面的内容, 从子页面中找到图片的下载地址  img -> src
#          3.下载图片

import requests
from bs4 import BeautifulSoup
import time

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
  chid_page_resp = requests.get(href)
  chid_page_resp.encoding = "utf-8"
  chid_page_resp_text = chid_page_resp.text
  # 从子页面中拿到图片的下载路径
  chid_page = BeautifulSoup(chid_page_resp_text, "html.parser")
  p = chid_page.find("p", align="center")
  img = p.find("img")
  src = img.get("src")
  # 下载图片
  img_resp = requests.get(src)
  # img_resp.content   # 这里拿到的是字节
  img_name = src.split("/")[-1]   # 通过 "/" 来切割, 并且取到最后一个内容
  with open("img/"+img_name, "wb") as file:
    file.write(img_resp.content)

  print("over!", img_name)
  time.sleep(1) # 设置1秒延迟

print("完成！")

