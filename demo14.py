# 项目14 爬取九怀中文网里的书架
# 项目介绍：登录 -> 得到cookie
#          带着cookie去请求到书架url -> 书架上的内容
#          必须得把上面的两个操作连起来
#          我们可以使用session进行请求 -> session你可以认为是一连串的请求，在这个过程中的cookie不会丢失
# 注意：程序不完整，账号和密码需要手动输入哦~~~

import requests

# 会话 (记录登录的cookie)
session = requests.session()

datas = { 
  "username": "账号",
  "password": "密码"
}

# 1.登录
url = "https://www.jiuhuaiwenxue.com/loginAction"
session.post(url, data=datas)
# resp = session.post(url, data=datas)
# print(resp.cookies)


# 2.拿书架上的内容
# 刚才的session中石油cookie的
resp = session.get('https://www.jiuhuaiwenxue.com/user/mybookcase')
print(resp.text)

# 如果直接使用requests.get()就会出现类似报错
# {"status":{"code":10103,"msg":"用户登录信息错误"},"time":1721463354000}


# 第二个方法 手动获取cookie
resp = requests.get('https://www.jiuhuaiwenxue.com/user/mybookcase', headers={
  "Cookie":"__qc_wId=363; pgv_pvid=1265613465; JSESSIONID=5138CD09D75FE0E64872B499D66F64DC"
})
print(resp.text)
