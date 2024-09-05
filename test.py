import requests
import re
import csv

url = "https://movie.douban.com/top250?start=0&filter="

headers = {
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=headers)
page = resp.text

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                r'.*?<br>.*?\n.*?\s+(?P<year>.*?)&nbsp'
                r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
text = obj.finditer(page)

with open("data.csv", "w", encoding="utf-8") as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(["name", "year", "score", "num"])

  for i in text:
    dic = i.groupdict()

    csv_writer.writerow(dic.values())
  
  # csv_writer.writerow(["name"])