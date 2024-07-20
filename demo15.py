# 项目15 爬取梨视频里的视频
# 项目介绍：由于网页页面里的视频链接和json文件里视频不一样，所以需要以下操作
#          1.拿到contID
#          2.拿到videoStatus返回的json，提取srcUrl里的信息
#          3.srcUrl里面的内容进行修改
#          4.下载视频
# 注意：每个网站都有自己的小心思，我们要谨慎，才不会踩坑，分析网页组成，才能更好的爬取内容
# 知识点：防盗链

import requests

# 网页视频页面
url = "https://www.pearvideo.com/video_1795270"
contID = url.split("_")[1]    # .strip() 屏蔽   .split() 切割

# json文件地址(videoStatus.js)
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.537376979352026"
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  # 防盗链： 溯源，当前请求的上一级是谁
  "Referer":url     # 请求过程: 1 -> 2 -> 3   1:requests  2:Referer  3:print
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contID}")   # .replace() 替换
# print(srcUrl)

# 下载视频
with open("a.mp4", "wb",) as f:
  f.write(requests.get(srcUrl).content)

# json文件里的视频链接
# https://video.pearvideo.com/mp4/short/20240712/cont-1795270-16032653-hd.mp4
# 真是的视频链接
# https://video.pearvideo.com/mp4/short/20240712/1721484205708-16032653-hd.mp4









