# 项目8 屠戮盗版天堂
# 项目介绍: 	1.定位到2024必看热片
#	           2.从2024必看热片中提取到子页面的链接地址
#            3.请求子页面的链接地址，拿到我们想要的下载地址
# 注意: 网站更新后，增加了反爬机制，请求头内要有 User-Agent 和 Cookie
#      如若程序失效，说明原网页的Cooike更新了，我们需要重新获取Cooike

import requests
import re
import urllib3   # urllib3 是一个用于 Python 的强大 HTTP 客户端库，提供了许多功能，使得在网络请求中更为简洁和高效
import csv

# 禁用 InsecureRequestWarning 的警告，InsecureRequestWarning(不安全请求警告)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)   # urllib3.disable_warnings 用于禁用由 urllib3 发出的警告信息

url = "https://www.dytt89.com/"

headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "Cookie":"__51vcke__KSHU1VNqce379XHB=65a32d95-2026-5c5e-8312-dfbcdd4651ea; __51vuft__KSHU1VNqce379XHB=1721102830894; Hm_lvt_8e745928b4c636da693d2c43470f5413=1721102831; HMACCOUNT=77CCD5AA8FC6EB68; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1721102831; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1721102831; guardok=Hju4Ta66KvVKGFBVP/jNspaAkrV2R5GL9pRu7bWG8m34BMbnjCIPdx/5QTXdanR5DJxtch0bbBNtPImYnTy58w==; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22bc98d519-bc6d-5f9a-975c-ba586f8cf22d%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201721134721279%2C%20%22ct%22%3A%201721132921279%7D; __51uvsct__KSHU1VNqce379XHB=5; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1721132921; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1721132921; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1721132921"
}

print("2024新片精品", "2024必看热片", "迅雷电影资源", "经典大片", "华语电视剧", "日韩电视剧", "欧美电视剧", "综艺&动漫")
choice = input("请选择爬取内容：")

# 提取到的电影链接, 保存到列表中
url_href_list = []

with open("data.csv", "w", encoding="utf-8") as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(["name", "download"])

  resp = requests.get(url, verify=False, headers=headers)    # verify=False 去除安全验证
  resp.encoding = "gb2312"  # 指定字符集

  obj1 = re.compile(rf"{choice}.*?<ul>(?P<ul>.*?)</ul>", re.S)    # (提取 2024必看热片)
  obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)   # (提取单个电影的链接)
  obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)   # (提取 电影名字 和 下载地址)

# 提取主页面内容 (提取 2024必看热片)
  result1 = obj1.finditer(resp.text)
  for i in result1:
    ul = i.group("ul")

    # 提取子页面链接 (提取 单个电影的链接)
    result2 = obj2.finditer(ul)
    for ii in result2:
      # 拼接子页面的url地址: 域名 + 子页面地址
      url_href = url + ii.group("href").strip("/")
      url_href_list.append(url_href)   # 把子页面链接保存起来

  # 提取子页面内容 (提取 电影名字 和 下载地址)
  for href in url_href_list:
    new_resp = requests.get(href, verify=False, headers=headers)
    new_resp.encoding = "gb2312"

    result3 = obj3.search(new_resp.text)

    csv_name = result3.group("movie")
    csv_down = result3.group("download")
    csv_writer.writerow([csv_name, csv_down])
        
    # dic = result3.groupdict()
    # csv_writer.writerow(dic.values())

    # print(result3.group("movie"))
    # print(result3.group("download"))
    # break

print(f"{choice}爬取成功")

# print(resp.text)
# /usr/local/lib/python3.10/dist-packages/urllib3/connectionpool.py:1099: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.dytt89.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
#   warnings.warn(
# 不安全请求警告：正在向主机“www.dytt89.com”发出未经验证的HTTPS请求。
# 强烈建议添加证书验证。请参阅：https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-警告
# 此时可以用到 urllib3 库，来消除 不安全请求警告，或者添加安全证书

# <script src="/_guard/auto.js"></script>
# 出现这个js文件，说明网页增加了反爬机制，我尝试了很多办法，最终在请求头内添加了Cookie，才成功拿到信息