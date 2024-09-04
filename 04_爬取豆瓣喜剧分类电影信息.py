# 项目4 爬取豆瓣喜剧分类电影信息
# 项目介绍：从网页中爬取到的戏剧电影的信息，以 json()数组 形式输出
# 注意：1.url地址，不要无脑复制url地址，多看一眼，多分析一下，哪一部分是地址，哪一部分是参数。
#      2.在控制台中 Payload 选项里，一定要注意 Query String Parameters 属性里 "start" 这个值
#        在往下刷新的时候，"start" 会递增，设置成递增值，则会爬取更多电影信息
# 总结：从这个项目可以得出，此时的网页是 客户端渲染

import requests

# url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
url = "https://movie.douban.com/j/chart/top_list"

# 数据在 Query String Parameters 属性，在控制台的 Payload 选项里
# 重新封装参数
parm = {
  "type": "24",
  "interval_id": "100:90",
  "action": "",
  "start": 0,
  "limit": 20
}

headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# get()请求用 params   post()请求用 data
# params 参数用于传递查询字符串参数。这些参数将附加到 URL 的末尾，形成一个完整的请求 URL
resp = requests.get(url, params=parm, headers=headers)

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
# print(resp.request.url)

# 输出为空，说明网页有反爬
# 需要设置请求头
# print(resp.text)

# 输出json()数组
# print(resp.text)

# 提取 电影名称 和 演员表
content = resp.json()
for i in content:
  name = i['title']
  performer = i['actors']
  print("电影名称：", name)
  print("演员：", performer)
  print(" ")

#释放资源
resp.close()