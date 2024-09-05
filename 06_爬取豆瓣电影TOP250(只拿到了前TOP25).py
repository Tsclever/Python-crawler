# 项目6 爬取豆瓣电影TOP250(只拿到了前TOP25)
# 项目流程: 1.通过requests库拿到页面源代码 
#          2.通过re模块来提取想要的有效信息
#          3.通过csv模块来保存数据, 用于读取和写入CSV（逗号分隔值）文件
# 注意: Python 自带的标准库中包含了 re 模块和 csv 模块

import requests
import re
import csv

url = "https://movie.douban.com/top250?start=0&filter="

#定义请求头，模拟浏览器请求
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
# 发送GET请求获取页面源代码
resp = requests.get(url, headers=headers)
page = resp.text

# 使用正则表达式解析数据
# r 在 Python 中用于表示原始字符串。在原始字符串中, 反斜杠 (\) 不会被视为转义字符, 它会按照字面意义被解释。
# 我的理解: 声明 我要在字符串中使用 正则表达式了
# re.S  让 . 能匹配换行符
obj = re.compile(r'<li>.*?<div class="item">'
                r'.*?<span class="title">(?P<name>.*?)</span>'
                r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'   # 第二种去去掉空格的方法 r'.*?<br>.*?\n.*?\s+(?P<year>.*?)&nbsp'
                r'.*?</p>.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                r'.*?<span>(?P<num>.*?)人评价</span>', re.S)   

# 开始匹配, 找到所有匹配的内容, 返回的是迭代器
text = obj.finditer(page)

# 打开csv文件, 并准备写入数据
with open("data.csv", mode="w", encoding="utf-8") as file:
  csv_writer = csv.writer(file)   # 创建一个csv.writer写入对象,调用csv,writer()方法,告诉python我要操作 file 里的数据了

  for i in text:
    # print(i.group("name"))
    # print("日期:",i.group("year").strip())   # strip() 剔除文本中多余的空白
    # print("评分:",i.group("score"))
    # print("评论数:",i.group("num"))
    dic = i.groupdict()   # 将匹配到的 命名分组 转换为 字典(就是把上面print()出来的数据转换为字典),
    dic['year'] = dic['year'].strip()   # 此时文本已经存入到 dic 字典中, 直接在内存中修改
    # print(dic)
    # 将字典中的值写入CSV文件
    csv_writer.writerow(dic.values())

print("豆瓣Top25成功爬取!")