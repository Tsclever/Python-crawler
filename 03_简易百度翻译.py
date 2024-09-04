# 项目3 简易百度翻译
# 项目介绍：在控制台中输入所需要翻译的英文单词, 在 百度翻译 中所翻译的结果, 会爬取下来, 最终以字典的形式展示出来
# 注意：1.需要获取抓包到的 隐示 网页链接, 而不是百度翻译所看到的 显示 链接
#      2.需要查看 https://fanyi.baidu.com/sug 文件里 Payload 选项, 然后查看 Form Data 属性里有哪些参数

import requests

# 在百度翻译中，抓包所查看到的 隐示链接 
url = "https://fanyi.baidu.com/sug"

name = input("请输入你要翻译的英文单词：")

# 查看抓包数据中的，Form Data 属性，在控制台的 Payload 选项里
data = {
  "kw" : name
}

# 发送post请求，发送的数据必须放在字典中，通过 data 参数进行传递
soup = requests.post(url, data=data)   # 需要注意的是，查看网页抓包里详细信息，
print(soup.json())   # 将服务区返回的内容直接处理成 json() -> dict{}字典