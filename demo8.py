# 项目8 屠戮盗版天堂
# 项目介绍: 	1.定位到2024必看片
#	           2.从2024必看片中提取到子页面的链接地址
#            3.请求子页面的链接地址，拿到我们想要的下载地址
# 注意: 网站更新后，增加了反爬机制，请求头内要有 User-Agent 和 Cookie

import requests
# import urllib3   # urllib3 是一个用于 Python 的强大 HTTP 客户端库，提供了许多功能，使得在网络请求中更为简洁和高效

# 禁用 InsecureRequestWarning 的警告，InsecureRequestWarning(不安全请求警告)
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)   # urllib3.disable_warnings 用于禁用由 urllib3 发出的警告信息

headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "Cookie":"guardok=Hju4Ta66KvVKGFBVP/jNsjdWcG+Z/rkbXtiD4BC5VZrGs6dqMgWJtrmjYF/ijqyFNcqheatzDyiXcHh7YHiQmg==; __51vcke__KSHU1VNqce379XHB=65a32d95-2026-5c5e-8312-dfbcdd4651ea; __51vuft__KSHU1VNqce379XHB=1721102830894; Hm_lvt_8e745928b4c636da693d2c43470f5413=1721102831; HMACCOUNT=77CCD5AA8FC6EB68; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1721102831; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1721102831; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22565e00f6-0cae-52a6-886d-dd89f76330b8%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201721110913375%2C%20%22ct%22%3A%201721109113375%7D; __51uvsct__KSHU1VNqce379XHB=2; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1721109114; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1721109114; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1721109114"
}

url = "https://www.dytt89.com/"
resp = requests.get(url, verify=False, headers=headers)    # verify=False 去除安全验证
resp.encoding = "gb2312"
print(resp.text)

# print(resp.text)
# /usr/local/lib/python3.10/dist-packages/urllib3/connectionpool.py:1099: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.dytt89.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
#   warnings.warn(
# 不安全请求警告：正在向主机“www.dytt89.com”发出未经验证的HTTPS请求。
# 强烈建议添加证书验证。请参阅：https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-警告
# 此时可以用到 urllib3 库，来消除 不安全请求警告，或者添加安全证书

# <script src="/_guard/auto.js"></script>
# 出现这个js文件，说明网页增加了反爬机制，我尝试了很多办法，selenium库失败，fscrape库失败，最终在请求头内添加了Cookie，才成功拿到信息