# 项目16 通过代理访问百度
# 原理：通过第三方的服务器去发送请求
# 注意：学习过程中，知道如何使用就行了，深入学习需反复考量
# 知识点：代理


import requests

# 寻找一个在法律范围内，能用的代理ip
# https://www.zdaye.com/free/3/ (在这个网站中，类型为透明的ip，是可用的)

# IP地址:端口
# 183.134.101.182:3128
proxy = {
  # "http":"",
  "https":"183.134.101.182:3128"
}

url = "https://www.baidu.com/"
resp = requests.get(url, proxies=proxy)
resp.encoding = "utf-8"
print(resp.text)

