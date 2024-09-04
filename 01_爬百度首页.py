# 项目一 爬百度首页
# 项目介绍：使用最原始的网络请求模块, 实现从网页爬取数据
# 程序流程：1.通过 Python 自带的 urllib.request, 引用 urlopen 函数, 读取目标链接
#          2.最终保存到 html 文件中

# 从 urllib.request 库中, 引用 urlopen 函数
from urllib.request import urlopen

# 网页地址
url = "http://www.baidu.com/"

# 读取 url 地址, 把读取的内容保存到 text 变量中
resp = urlopen(url)
text = resp.read()

# 打印网页的内容，以 utf-8 的格式
print(text.decode("utf-8"))

# 把读取的内容写入到 html 文件中
# 以 w(文本的形式) 写入 baidu.html 文件，若没有 baidu.html 文件 则创建 baidu.html 文件
with open("baidu.html", mode = "w", encoding=("utf-8")) as f:   # encoding=("utf-8") 用于数据写入
  f.write(text.decode("utf-8"))     # 写入获取到的网页代码，以 utf-8 所解码出来的 html + css + js 的源代码，decode("utf-8") 用于数据解码
print("baidu.html写入成功!")