# 项目一 爬百度首页

# 从 urllib.request 库中，引用 urlopen 函数
from urllib.request import urlopen

# 网页地址
url = "http://www.baidu.com/"

# 打开 url 地址，并读取内容
resp = urlopen(url)
html = resp.read()

# 打印网页的内容，以 utf-8 的格式
# print(html.decode("utf-8"))

# 打开 baidu.html 文件，以 w(文本的形式) 写入 baidu.html 文件，若没有 baidu.html 文件 则创建 baidu.html 文件
with open("baidu.html", mode = "w", encoding=("utf-8")) as f:   # encoding=("utf-8") 用于数据写入
  f.write(html.decode("utf-8"))     # 写入获取到的网页代码，以 utf-8 所解码出来的 html + css + js 的源代码，decode("utf-8") 用于数据解码
print("over!")