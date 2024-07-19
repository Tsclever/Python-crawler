# 项目13 爬取猪八戒官网
# 项目介绍: 猪八戒网是中国领先的服务众包平台
#          1.拿到页面源代码
#          2.提取和解析数据
# 注意: 一定要看仔细网页源代码中的层级关系

import requests
from lxml import etree

url = "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
# print(resp.text)

# 解析页面源代码
html = etree.HTML(resp.text)
# 拿到每一个服务商的div
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div/div[2]/div')
for i in divs:
  price = i.xpath("./div/div[3]/div[1]/span/text()")[0].strip("¥")   # 层级关系一定要看仔细, [0] 表示从返回的列表中获取第一个元素。这是因为 xpath 方法的返回值始终是一个列表，即使只有一个匹配项。
  title = "SAAS".join(i.xpath("./div/div[3]/div[2]/a/span/text()"))   # 层级关系一定要看仔细  "SAAS".join 将可迭代对象中的元素连接成一个字符串
  com_name = i.xpath("./div/div[5]/div/div/div/text()")[0]
  print(price,title,com_name)