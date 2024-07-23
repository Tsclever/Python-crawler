# 项目20 爬取北京新发地(运用了线程池)
# 项目介绍: 1.如何提取单个页面的数据
#          2.上线程池,多个页面同时抓取

import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor   # ThreadPoolExecutor线程池, ProcessPoolExecutor进程池
import csv
import json
import time

def download_one_page(url):

  with open("data.csv", "w", encoding="utf-8") as file:
    csvwrite = csv.writer(file)
    csvwrite.writerow(['分类', '品名', '最低价', '平均价', '最高价', '产地', '单位', '发布日期'])
    
    for current in range(1,201):
      data = {
        "current": str(current)
      }
      resp = requests.get(url, params=data)
      resp_text = resp.text
      data = json.loads(resp_text)   # .loads()用于将 JSON 格式的字符串解码成 Python 数据结构
      # print(data)

      comments = data['list']   # 拿到json中list里所有的数据
      time.sleep(0.5)   # 设置0.5延迟

      for i in comments:   # 遍历数据
        # print(i)
        row = [
                  i['prodCat'], i['prodName'], i['lowPrice'], i['avgPrice'],
                  i['highPrice'], i['place'], i['unitInfo'], i['pubDate'].split(" ")[0]
              ]
        csvwrite.writerow(row)
      print(f"第{current}页提取成功")

def main():
  with ThreadPoolExecutor(50) as T:
    T.submit(download_one_page, "http://www.xinfadi.com.cn/getPriceData.html")   # .submit(函数, 参数)

if __name__ == '__main__':
  main()
