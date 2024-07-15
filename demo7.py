# 项目7 爬取豆瓣电影TOP250(成功拿到Top250)
# 项目介绍: 1.通过requests库拿到页面源代码 
#          2.通过re模块来提取想要的有效信息
#          3.通过csv模块来保存数据, 用于读取和写入CSV（逗号分隔值）文件
# 注意: 一定要注意 缩进！缩进！缩进！

import requests
import re
import csv

url = "https://movie.douban.com/top250?"

headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


with open("data.csv", mode="w", encoding="utf-8") as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(["name", "year", "score", "num"])   # csv有个特性，表头类似于导航栏，所以可以添加一个表头，不然第一个数据就是表头了

  for start in range(0, 250, 25):
    parm = {
    "start": start,
    "filter": "",
    }

    resp = requests.get(url, params=parm, headers=headers)
    page = resp.text

    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?</p>.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)</span>', re.S)

    text = obj.finditer(page)

    for i in text:
      dic = i.groupdict()
      dic["year"] = dic["year"].strip()
      csv_writer.writerow(dic.values())

print("over!")

