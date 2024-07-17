# 项目9 爬取农产品市场行情
# 项目介绍: 1.获取网页的源代码
#          2.使用bs4库进行数据解析
#          3.提取我们想要的行情数据
#          4.存入到data.csv文件中
#注意: 这一个项目涉及到了bs4库的使用, 需要我们多加练习。

import requests
from bs4 import BeautifulSoup
import csv

url = "http://sc.cqnync.cn/marketSta/?vexp=3&classId=3"
resp = requests.get(url)

with open("data.csv", "w", encoding="utf-8") as file:
  # 声明csv
  csv_writer = csv.writer(file)
  csv_writer.writerow(["name","location","year","money","kid"])

  # 解析数据
  # 把页面源代码交给BeautifulSoup进行处理, 生成BeautifulSoup对象
  page = BeautifulSoup(resp.text, "html.parser")   # 声明resp.text 是 html
  # 从bs对象中查找数据
  # find(标签, 属性=值) 只找一个
  # find_all(标签, 属性=值) 找全部

  # table = page.find("table", class_="list")   # class是Python的关键字, class_代表的是html里的class
  table = page.find("table", attrs={"class":"list"})   # 等同于上一行, 可以避免使用class_
  # 拿到所有数据行
  trs = table.find_all("tr")[1:]
  for tr in trs:   # 每一行
    tds = tr.find_all("td")
    name = tds[0].text   # .text 表示拿到被标签标记的内容 <td>内容</td>
    loc = tds[1].text   # .text 表示拿到被标签标记的内容 <td>内容</td>
    year = tds[2].text   # .text 表示拿到被标签标记的内容 <td>内容</td>
    money = tds[4].text   # .text 表示拿到被标签标记的内容 <td>内容</td>
    kid = tds[6].text   # .text 表示拿到被标签标记的内容 <td>内容</td>
    csv_writer.writerow([name,loc,year,money,kid])
print("over!")