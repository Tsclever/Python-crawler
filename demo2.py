# 项目2 简易搜狗搜索引擎
# 项目介绍：在控制台中输入 明星 名字，所搜索到的结果会保存到以 明星名字 命名的 txt 文件中

import requests
from bs4 import BeautifulSoup

# 
query = input("请输入一个你喜欢的明星：")

# url 地址栏一定是用的 get 方法进行提交
# f 字符串，运行字符串嵌入表达式中
url = f'https://www.sogou.com/web?ie=UTF-8&query={query}'

# 如若出现了访问不正常，则需要去浏览器里的控制台查看 User-Agent
# 模拟人来访问网页，发起 get 请求
# 请求头
RequestHeaders = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# response 响应
resp = requests.get(url, headers=RequestHeaders)   # 处理了一个小小的反爬

# <Response [200]>  相应状态 ：200
# print(resp)

# 获取页面源代码
# 在没有加入请求头之前
# 此时出现了<p class="p2">用户您好，我们的系统检测到您网络中存在一场访问请求</br>此验证码用于确认这些请求是您的正常行为而不是自动程序发出的，需要您协助验证。</p>
# 并没有按照原本的计划，打印网页应该出现的内容，说明了访问不正常
# print(resp.text)

# 加了请求头之后，成功打印网页源代码
# 实现了简易的搜哦框
# print(resp.text)

# 检查响应状态码
if resp.status_code == 200:
    # 解析HTML页面
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # 获取所有文本内容
    page_text = soup.get_text()
    
    # 剔除文本中的多余空白和缩进
    # 分割文本，去除每一行两端的空白，再将非空行重新连接
    clean_text = "\n".join(line.strip() for line in page_text.splitlines() if line.strip())
    
    # 将清理后的文本内容写入到文件
    with open(f"{query}档案.txt", "w", encoding="utf-8") as file:
        file.write(clean_text)
    
    print(f"页面文本内容已成功写入到{query}档案.txt文件中。")
else:
    print(f"请求失败，状态码：{resp.status_code}")