# 项目20 爬取北京新发地(运用了线程池)
# 项目介绍: 1.如何提取单个页面的数据
#          2.上线程池,多个页面同时抓取
# 测试: 经过测试, 这个网站稍微爬的快一丢丢就503了~~~大概是前辈们把这个网站轰炸了吧~~~

import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor   # ThreadPoolExecutor线程池, ProcessPoolExecutor进程池
import csv
import json
import time

def download_one_page(url, data, file, mouth):

    resp = requests.get(url, params=data)
    # print(resp)
    resp_text = resp.text
    data_list = json.loads(resp_text)   # .loads()用于将 JSON 格式的字符串解码成 Python 数据结构
    # print(data)

    comments = data_list['list']   # 拿到json中list里所有的数据
    time.sleep(1)   # 设置1秒延迟

    for i in comments:   # 遍历数据
      # print(i)
      row = [
                i['prodCat'], i['prodName'], i['lowPrice'], i['avgPrice'],
                i['highPrice'], i['place'], i['unitInfo'], i['pubDate'].split(" ")[0]
            ]
      
      # 声明csv对象
      csvwrite = csv.writer(file)
      csvwrite.writerow(row)

    print(f"第{mouth}页提取成功")

def main():
  url = "http://www.xinfadi.com.cn/getPriceData.html"

  with open("data.csv", "w", encoding="utf-8") as file:
    csvwrite = csv.writer(file)
    csvwrite.writerow(['分类', '品名', '最低价', '平均价', '最高价', '产地', '单位', '发布日期'])

    # 创建线程池
    with ThreadPoolExecutor(3) as T:   # 创建有3个线程的线程池
      for current in range(1,21):   # 遍历20页的数据
        data = {"current": str(current)}
        mouth = current
        # 把下载任务提交给线程池
        T.submit(download_one_page, url, data, file, mouth)   # .submit(函数, 参数)

if __name__ == '__main__':
  main()
